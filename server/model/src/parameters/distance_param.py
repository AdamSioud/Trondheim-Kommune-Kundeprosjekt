import pandas as pd
import geopandas as gpd
import shapely
from shapely.geometry import Point
from server.model.src.parameters.param_interface import ParamInterface
from server.model.src.data.data import Data


class DistanceParam(ParamInterface):
    """Class for calculating score for age-parameter"""
    def __init__(self):
        super().__init__()
        self.INPUT_NAME = "distance_input"

    def give_score(self, bydel: shapely.geometry.multipolygon.MultiPolygon, pos: shapely.geometry.point.Point,
                   min_distance=0.02, increment=0.01) -> int:
        """
        Add converter? To timeconsuming, save it for later
        1 degree is approx 111.1 km
        """
        center = bydel.centroid
        distance = pos.distance(center)
        limit = min_distance
        for p in range(5, 0, -1):
            if distance <= limit:
                return p
            limit += increment
        return 0

    def make_df_copy(self) -> gpd.GeoDataFrame:
        """Makes a copy of the general-dataframe and adds the geometry-column."""
        print(type(self.data.add_geometry_column(self.data.GENERAL_DF).copy()))
        return self.data.add_geometry_column(self.data.GENERAL_DF).copy()

    def validate_input(self, inp: dict) -> None:
        self.validate_args(inp, ['position', 'weight'])
        self.validate_weight(inp)
        # TODO: validate 'position'

    def calculate_score(self, inp: dict) -> pd.DataFrame:
        """
        Calculates the score for all the zones, using give_score on each zone. Then multiplies it with the
        'weight'-input.
        :param inp: The input on format: 'age_input' = { 'selected': [], 'percent': int, 'weight': int }
        :return: DataFrame with the score.
        """
        self.validate_input(inp)
        result = self.make_df_copy()
        pos = inp.get('position')
        weight = inp['weight']
        result['score'] = result['geometry'].apply(lambda x: self.give_score(x, pos) * weight)
        print(type(result.filter(items=['score'])))
        return result.filter(items=['score'])
