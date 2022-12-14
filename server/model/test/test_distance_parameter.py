import unittest
from shapely.speedups._speedups import Point
from unittest.mock import MagicMock
from server.model.src.parameters.distance_parameter import DistanceParameter
import geopandas as gpd


class TestDistanceParameter(unittest.TestCase):

    def setUp(self) -> None:
        self.dp = DistanceParameter()
        DistanceParameter.make_df_copy = MagicMock()
        DistanceParameter.make_df_copy.return_value = gpd.read_file('mock_data/distance.json')

    def test_give_score(self):
        pass

    def test_calculate_score(self):
        inp = {
            "position": Point(10.39628304564158, 63.433247153410214),
            "weight": 1
        }
        res = self.dp.calculate_score(inp)
        self.assertEqual(res['score'][0], 4)
        self.assertEqual(res['score'][1], 1)
        self.assertEqual(res['score'][2], 5)
        self.assertEqual(res['score'][3], 5)
        self.assertEqual(res['score'][4], 5)

        inp = {
            "position": Point(10.39628304564158, 63.433247153410214),
            "weight": 3
        }
        res = self.dp.calculate_score(inp)
        self.assertEqual(res['score'][0], 12)
        self.assertEqual(res['score'][1], 3)
        self.assertEqual(res['score'][2], 15)
        self.assertEqual(res['score'][3], 15)
        self.assertEqual(res['score'][4], 15)

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
