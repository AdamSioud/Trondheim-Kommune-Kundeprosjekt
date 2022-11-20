from generate_geojson.configuration import *
from generate_geojson.renaming import *
from generate_geojson.build_files import create_geodataframe, create_trondheim_json, create_interval_dataframe
import json
import geopandas as gpd

# Generate GeoJSON for each zone
geojson = gpd.read_file(link_geo_json_file)
gdf = create_geodataframe(properties, sheets, geojson, final_columns, converters)


gdf["zoneName"] = gdf["Levekårsnavn"]
gdf = gdf.drop(columns=["Levekårsnavn"])

gdf["age"].apply(rename_age)
gdf["price"].apply(rename_price)
gdf["neighborhood"].apply(rename_neighborhood)


gdf.to_file("data.geojson", driver="GeoJSON")


# Generate general data for Trondheim
data_trondheim = create_trondheim_json(properties_trondheim, sheets, final_columns_trondheim, converters_trondheim,
                                       renaming)

with open("data_general.json", "w") as f:
    json.dump(data_trondheim, f)

# Generate interval data
df_i = create_interval_dataframe(properties_interval, sheets_interval, final_names_interval, converters_interval)
df_i["neighborhood"].apply(rename_interval)
df_i.to_json("data_interval.json")
