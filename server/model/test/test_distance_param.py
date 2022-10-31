import unittest
from shapely.speedups._speedups import Point
from unittest.mock import MagicMock
from server.model.src.parameters.distance_param import DistanceParam
from server.model.src.data.data import Data
import pandas as pd
import geopandas as gpd


class TestDistanceParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.dp = DistanceParam(self.data)
        DistanceParam.make_df_copy = MagicMock()
        DistanceParam.make_df_copy.return_value = gpd.read_file('mock_data/distance.json')

    def test_give_score(self):
        pass

    def test_calculate_score(self):
        inp = {
            "position": Point(10.39628304564158, 63.433247153410214),
            "weight": 1
        }
        res = self.dp.calculate_score(inp)
        self.assertEqual(res['Score'][0], 4)
        self.assertEqual(res['Score'][1], 1)
        self.assertEqual(res['Score'][2], 5)
        self.assertEqual(res['Score'][3], 5)
        self.assertEqual(res['Score'][4], 5)

        inp = {
            "position": Point(10.39628304564158, 63.433247153410214),
            "weight": 3
        }
        res = self.dp.calculate_score(inp)
        self.assertEqual(res['Score'][0], 12)
        self.assertEqual(res['Score'][1], 3)
        self.assertEqual(res['Score'][2], 15)
        self.assertEqual(res['Score'][3], 15)
        self.assertEqual(res['Score'][4], 15)

        inp = {
            "position": Point(10.39628304564158, 63.433247153410214),
            "weight": 0
        }
        self.assertRaises(ValueError, self.dp.calculate_score, inp)

        inp = {
            "position": Point(10.39628304564158, 63.433247153410214),
            "weight": 6
        }
        self.assertRaises(ValueError, self.dp.calculate_score, inp)

        inp = {
            "weight": 3
        }
        self.assertRaises(ValueError, self.dp.calculate_score, inp)


if __name__ == '__main__':
    unittest.main()
