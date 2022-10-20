import pandas as pd
import geopandas as gpd
from pathlib import Path
import json


DATASETS = ('Ages', 'Price', 'Nærmiljø')
GENERAL_PROPERTIES = ('Levekårsone-nummer', 'Levekårsnavn')
GEOMETRY_COULUMN = 'geometry'


def get_datasets(gdf):
    # dict of dataframes in DATASETS
    dfs = {}
    for key in DATASETS:
        # gdfs[key] = pd.concat([generalDataFrame, pd.json_normalize(gdf[key])], axis=1)
        dfs[key] = pd.json_normalize(gdf[key])
    return dfs


def get_general_df(gdf):
    # General df containing GENERAL_PROPERTIES
    result = {}
    for key in GENERAL_PROPERTIES:
        result[key] = gdf[key]
    return pd.DataFrame(result)


def get_geometry_df(gdf):
    return gdf[GEOMETRY_COULUMN]


def read_geojson(file_name: str):
    gdf = gpd.read_file(file_name)
    dfs = get_datasets(gdf)
    general_df = get_general_df(gdf)
    geo_clm = get_geometry_df(gdf)
    return dfs, general_df, geo_clm


def read_json(file_name: str):
    df_i = pd.read_json(file_name)
    df_is = {}
    for key in df_i.columns:
        df_is[key] = pd.json_normalize(df_i[key])
    return df_is


class Data:
    path_base = Path(__file__).resolve().parent
    DFS, GENERAL_DF, GEOMETRY = read_geojson(path_base / 'data2.geojson')
    INTERVAL_DFS = read_json(path_base / 'data_interval.json')

    def add_geometry_column(self, df):
        return gpd.GeoDataFrame(df, geometry=self.GEOMETRY)

    def add_general_properties(self, df):
        df = pd.concat([self.GENERAL_DF, df], axis=1)
        return df

    def get_zone_by_id(self, i: int) -> str:
        with open(self.path_base / 'data2.geojson', "r") as fp:
            data = json.loads(fp.read())
        try:
            data = data['features'][i]['properties']
            print(len(data))
            return json.dumps(data)
        except IndexError:
            raise IndexError(f'id out of range. Has to be between 0 and {len(data["features"]) - 1}')