import geopandas as gpd
import numpy as np
import pandas as pd
from server.model.src.parameters.age_parameter import AgeParameter
from server.model.src.parameters.culture_parameter import CultureParameter
from server.model.src.parameters.distance_parameter import DistanceParameter
from server.model.src.parameters.grocery_parameter import GroceryParameter
from server.model.src.parameters.outdoor_parameter import OutdoorParameter
from server.model.src.parameters.price_parameter import PriceParameter
from server.model.src.parameters.safety_parameter import SafetyParameter
from server.model.src.parameters.transport_parameter import TransportParameter
from server.model.src.parameters.walkway_parameter import WalkwayParameter
from server.model.src.parameters.well_being_parameter import WellBeingParameter
from server.model.src.parameters.noise_parameter import NoiseParameter
from server.model.src.data.data_manager import DataManager


class MapManager:
    """The model doing calculation for all the parameters"""

    def __init__(self):
        self.data_manager = DataManager()
        self.parameters = [
            PriceParameter(),
            AgeParameter(),
            DistanceParameter(),
            WellBeingParameter(),
            SafetyParameter(),
            CultureParameter(),
            OutdoorParameter(),
            TransportParameter(),
            WalkwayParameter(),
            GroceryParameter(),
            SafetyParameter(),
            NoiseParameter()
        ]

    def make_df_copy(self):
        """Makes a copy of the general DataFrame."""
        return self.data_manager.GENERAL_DF.copy()

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
        tmp = result['score'][0]
        result['score'] = np.round_(100 * (result['score'] - result['score'].min()) / (result['score'].max()
                                                                                       - result['score'].min()), 1)
        if result['score'].isnull().values.any():
            if tmp == 0:
                result['score'] = 0
            else:
                result['score'] = 100
        result['score'] = result['score'].astype(float)
        return result

    def generate_map(self, param_input: dict) -> gpd.GeoDataFrame:
        """Generates a GeoDataFrame from the result from calculate_scores"""
        result = self.calculate_scores(param_input)
        return gpd.GeoDataFrame(result, geometry=self.data_manager.GEOMETRY)

    def get_zone_by_id(self, i: int):
        """Gets the data of a single zone by its id."""
        return self.data_manager.get_zone_by_id(i)
