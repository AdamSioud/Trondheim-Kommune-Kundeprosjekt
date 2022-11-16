import pandas as pd
import geopandas as gpd
from pathlib import Path
import json
from typing import Tuple

# Keys of datasets currently in data.geojson
DATASETS = ('age', 'price', 'neighborhood')
# Name of the general property column
GENERAL_PROPERTY = 'zoneName'
# Name of the geometry column
GEOMETRY_COLUMN = 'geometry'


def get_datasets(gdf: gpd.GeoDataFrame) -> dict:
    """Gets the datasets from the geojson file and puts them in a dictionary."""
    dfs = {}
    for key in DATASETS:
        dfs[key] = pd.json_normalize(gdf[key])
    return dfs


def get_general_df(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    """Gets the general DataFrame containing zoneName"""
    return pd.DataFrame(gdf[GENERAL_PROPERTY])


def get_geometry_column(gdf: gpd.GeoDataFrame) -> gpd.GeoSeries:
    """Gets the geometry column containing the polygons for each zone"""
    return gdf[GEOMETRY_COLUMN]


def read_geojson(file_path: str) -> Tuple[dict, pd.DataFrame, gpd.GeoSeries]:
    """Reads the GeoJSON file containing all the data and reformat it.
    :param file_path: The file path.
    :return: dfs: dict containing all relevant DataFrames, general_df: DataFrame containing the general properties,
    geo_clm: the geometry column.
    """
    gdf = gpd.read_file(file_path)
    dfs = get_datasets(gdf)
    general_df = get_general_df(gdf)
    geo_clm = get_geometry_column(gdf)
    return dfs, general_df, geo_clm


def read_json(file_path: str) -> dict:
    """Reads the JSON file containing the intervals and stores them in a dict.
    :param file_path: The file path.
    :return: dict containing the intervals.
    """
    df_i = pd.read_json(file_path)
    df_is = {}
    for key in df_i.columns:
        df_is[key] = pd.json_normalize(df_i[key])
    return df_is


class DataManager:
    """Class for accessing the data used in the backend."""
    instance = None
    path_base = Path(__file__).resolve().parent
    DFS, GENERAL_DF, GEOMETRY = read_geojson(str(path_base / 'data.geojson'))
    INTERVAL_DFS = read_json(str(path_base / 'data_interval.json'))

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(DataManager, cls).__new__(cls)
        return cls.instance

    def add_geometry_column(self, df: pd.DataFrame) -> gpd.GeoDataFrame:
        """Adds the geometry column to the DataFrame"""
        return gpd.GeoDataFrame(df, geometry=self.GEOMETRY)

    def add_general_properties(self, df: pd.DataFrame) -> pd.DataFrame:
        """Adds the general columns to the DataFrame"""
        df = pd.concat([self.GENERAL_DF, df], axis=1)
        return df

    def get_zone_by_id(self, i: int) -> str:
        """Returns all the date for a single zone
        :param i: the index of the zone
        :return: a JSON string with the data"""
        with open(self.path_base / 'data.geojson', "r") as fp:
            data = json.loads(fp.read())
        try:
            data = data['features'][i]['properties']
            return json.dumps(data)
        except IndexError:
            raise IndexError(f'id out of range. Has to be between 0 and {len(data["features"]) - 1}')
