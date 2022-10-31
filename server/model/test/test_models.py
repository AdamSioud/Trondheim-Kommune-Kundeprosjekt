import unittest
from unittest.mock import MagicMock
from shapely.geometry import Point
from server.model.src.models import Model
from server.model.src.parameters.age_param import AgeParam
import pandas as pd
import geopandas as gpd
from server.model.src.parameters.distance_param import DistanceParam
from server.model.src.parameters.price_param import PriceParam
from server.model.src.parameters.environment_param_interface import EnvironmentParam


class TestModel(unittest.TestCase):
    def setUp(self) -> None:
        self.m = Model()
        Model.make_df_copy = MagicMock()
        Model.make_df_copy.return_value = pd.read_json('mock_data/general_df.json')

        AgeParam.make_df_copy = MagicMock()
        AgeParam.make_df_copy.return_value = pd.read_json('mock_data/ages.json')

        DistanceParam.make_df_copy = MagicMock()
        DistanceParam.make_df_copy.return_value = gpd.read_file('mock_data/distance.json')

        EnvironmentParam.get_interval = MagicMock()
        EnvironmentParam.get_interval.return_value = [0.75, 0.8, 0.85, 0.9]
        EnvironmentParam.make_df_copy = MagicMock()
        EnvironmentParam.make_df_copy.return_value = pd.read_json('mock_data/nærmiljø.json')

        PriceParam.make_df_copy = MagicMock()
        PriceParam.make_df_copy.return_value = pd.read_json('mock_data/price.json')

    def test_calculate_score(self):
        par_input = {
            "age_input": {
                "selected": ['underage (0-17)', 'young adult (18-34)'],
                "percent": 10,
                "weight": 4
            },
            "price_input": {
                "budget": 2400000,
                "weight": 4
            },
            "distance_input": {
                "position": Point(10.39628304564158, 63.433247153410214),
                "weight": 4
            },
            "environment": {
                "well_being_input": {
                    "weight": 4
                },
                "safety_input": {
                    "weight": 1
                },
                "culture_input": {
                    "weight": 4
                },
                "outdoor_input": {
                    "weight": 4
                },
                "transport_input": {
                    "weight": 4
                },
                "walkway_input": {
                    "weight": 4
                },
                "grocery_input": {
                    "weight": 4
                },
                "noise_input": {
                    "weight": 4
                }
            }
        }
        res = self.m.calculate_scores(par_input)
        self.assertEqual(res['Score'][0], 162)
        self.assertEqual(res['Score'][1], 146)
        self.assertEqual(res['Score'][2], 162)
        self.assertEqual(res['Score'][3], 161)
        self.assertEqual(res['Score'][4], 162)

        par_input = {
            "age_input": {
                "selected": ['underage (0-17)', 'young adult (18-34)'],
                "percent": 10,
                "weight": 4
            },
            "price_input": {
                "budget": 2400000,
                "weight": 4
            },
            "distance_input": {
                "position": Point(10.39628304564158, 63.433247153410214),
                "weight": 4
            }
        }
        res = self.m.calculate_scores(par_input)
        self.assertEqual(res['Score'][0], 36)
        self.assertEqual(res['Score'][1], 24)
        self.assertEqual(res['Score'][2], 40)
        self.assertEqual(res['Score'][3], 40)
        self.assertEqual(res['Score'][4], 40)

        par_input = {}
        res = self.m.calculate_scores(par_input)
        self.assertEqual(res['Score'][0], 0)
        self.assertEqual(res['Score'][1], 0)
        self.assertEqual(res['Score'][2], 0)
        self.assertEqual(res['Score'][3], 0)
        self.assertEqual(res['Score'][4], 0)

    def test_get_zone_by_id(self):
        pass
