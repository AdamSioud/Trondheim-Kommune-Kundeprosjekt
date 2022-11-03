import geopandas as gpd
import pandas as pd
from server.model.src.parameters.age_param import AgeParam
from server.model.src.parameters.culture_param import CultureParam
from server.model.src.parameters.distance_param import DistanceParam
from server.model.src.parameters.grocery_param import GroceryParam
from server.model.src.parameters.outdoor_param import OutdoorParam
from server.model.src.parameters.price_param import PriceParam
from server.model.src.parameters.safety_param import SafetyParam
from server.model.src.parameters.transport_param import TransportParam
from server.model.src.parameters.walkway_param import WalkwayParam
from server.model.src.parameters.well_being_param import WellBeingParam
from server.model.src.parameters.noise_param import NoiseParam
from server.model.src.data.data import Data


class Model:
    """The model doing calculation for all the parameters"""
    def __init__(self):
        self.data = Data()
        self.parameters = [
            PriceParam(self.data),
            AgeParam(self.data),
            DistanceParam(self.data),
            WellBeingParam(self.data),
            SafetyParam(self.data),
            CultureParam(self.data),
            OutdoorParam(self.data),
            TransportParam(self.data),
            WalkwayParam(self.data),
            GroceryParam(self.data),
            SafetyParam(self.data),
            NoiseParam(self.data)
        ]

    def make_df_copy(self):
        """Makes a copy of the general DataFrame."""
        return self.data.GENERAL_DF.copy()

    def calculate_scores(self, param_input: dict) -> pd.DataFrame:
        """
        Calculates the score for each zone by adding the score for each parameter. Then Normalizes the score from 0-100.
        :param param_input: The input on format: { inp1: {...}, inp2: {...}, ... }
        :return: DataFrame with the scores.
        """
        result = self.make_df_copy()
        result['score'] = 0
        for param in self.parameters:
            if param.INPUT_NAME in param_input.keys():
                inp = param_input[param.INPUT_NAME]
                tmp = param.calculate_score(inp)
                result['score'] = result['score'].add(tmp['score'], fill_value=0)
            elif 'environment' in param_input.keys():
                if param.INPUT_NAME in param_input['environment'].keys():
                    inp = param_input['environment'][param.INPUT_NAME]
                    tmp = param.calculate_score(inp)
                    result['score'] = result['score'].add(tmp['score'], fill_value=0)
        # result['score'] = pd.qcut(result['score'], 5, labels=False, duplicates='drop')
        result['score'] = result['score'].astype(float)
        return result

    def generate_map(self, param_input: dict) -> gpd.GeoDataFrame:
        """Generates a GeoDataFrame from the result from calculate_scores"""
        result = self.calculate_scores(param_input)
        return gpd.GeoDataFrame(result, geometry=self.data.GEOMETRY)

    def get_zone_by_id(self, i: int):
        """Gets the data of a single zone by its id."""
        return self.data.get_zone_by_id(i)
