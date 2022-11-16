import unittest
from unittest.mock import MagicMock
from shapely.geometry import Point
from server.model.src.map_manager import MapManager
from server.model.src.parameters.age_parameter import AgeParameter
import pandas as pd
import geopandas as gpd
from server.model.src.parameters.distance_parameter import DistanceParameter
from server.model.src.parameters.price_parameter import PriceParameter
from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter


class TestMapManager(unittest.TestCase):
    def setUp(self) -> None:
        self.m = MapManager()
        MapManager.make_df_copy = MagicMock()
        MapManager.make_df_copy.return_value = pd.read_json('mock_data/general_df.json')

        AgeParameter.make_df_copy = MagicMock()
        AgeParameter.make_df_copy.return_value = pd.read_json('mock_data/age.json')

        DistanceParameter.make_df_copy = MagicMock()
        DistanceParameter.make_df_copy.return_value = gpd.read_file('mock_data/distance.json')

        AbstractNeighborhoodParameter.get_interval = MagicMock()
        AbstractNeighborhoodParameter.get_interval.return_value = [0.75, 0.8, 0.85, 0.9]
        AbstractNeighborhoodParameter.make_df_copy = MagicMock()
        AbstractNeighborhoodParameter.make_df_copy.return_value = pd.read_json('mock_data/neighborhood.json')

        PriceParameter.make_df_copy = MagicMock()
        PriceParameter.make_df_copy.return_value = pd.read_json('mock_data/price.json')

    def test_calculate_score(self):
        par_input = {
            "age_input": {
                "selected": ['0-17', '18-34'],
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
        self.assertEqual(res['score'][0], 100)
        self.assertEqual(res['score'][1], 0)
        self.assertEqual(res['score'][2], 100)
        self.assertEqual(res['score'][3], 93.8)
        self.assertEqual(res['score'][4], 100)

        par_input = {
            "age_input": {
                "selected": ['0-17', '18-34'],
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
        self.assertEqual(res['score'][0], 75)
        self.assertEqual(res['score'][1], 0)
        self.assertEqual(res['score'][2], 100)
        self.assertEqual(res['score'][3], 100)
        self.assertEqual(res['score'][4], 100)

        par_input = {}
        res = self.m.calculate_scores(par_input)
        self.assertEqual(res['score'][0], 0)
        self.assertEqual(res['score'][1], 0)
        self.assertEqual(res['score'][2], 0)
        self.assertEqual(res['score'][3], 0)
        self.assertEqual(res['score'][4], 0)

        par_input = {
            "age_input": {
                "selected": ['0-17', '18-34'],
                "percent": 1,
                "weight": 4
            }
        }
        res = self.m.calculate_scores(par_input)
        self.assertEqual(res['score'][0], 100)
        self.assertEqual(res['score'][1], 100)
        self.assertEqual(res['score'][2], 100)
        self.assertEqual(res['score'][3], 100)
        self.assertEqual(res['score'][4], 100)


    def test_get_zone_by_id(self):
        # TODO: make tests
        pass


if __name__ == '__main__':
    unittest.main()