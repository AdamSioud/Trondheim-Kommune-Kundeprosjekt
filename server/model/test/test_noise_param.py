import unittest
from server.model.src.parameters.noise_param import NoiseParam, NoiseTrafficParam, NoiseOtherParam
from server.model.src.data.data import Data
from unittest.mock import MagicMock
import pandas as pd


class TestNoiseParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.np = NoiseParam(self.data)
        NoiseOtherParam.get_interval = MagicMock()
        NoiseOtherParam.get_interval.return_value = [0.75, 0.8, 0.85, 0.9]
        NoiseOtherParam.make_df_copy = MagicMock()
        NoiseOtherParam.make_df_copy.return_value = pd.read_json('mock_data/nærmiljø.json')

        NoiseTrafficParam.get_interval = MagicMock()
        NoiseTrafficParam.get_interval.return_value = [0.75, 0.8, 0.85, 0.9]
        NoiseTrafficParam.make_df_copy = MagicMock()
        NoiseTrafficParam.make_df_copy.return_value = pd.read_json('mock_data/nærmiljø.json')

    def test_calculate_score(self):
        inp = {
            "weight": 1
        }
        res = self.np.calculate_score(inp)
        self.assertEqual(res['Score'][0], 5)
        self.assertEqual(res['Score'][1], 5)
        self.assertEqual(res['Score'][2], 5)
        self.assertEqual(res['Score'][3], 5)
        self.assertEqual(res['Score'][4], 5)

        inp = {
            "weight": 3
        }
        res = self.np.calculate_score(inp)
        self.assertEqual(res['Score'][0], 15)
        self.assertEqual(res['Score'][1], 15)
        self.assertEqual(res['Score'][2], 15)
        self.assertEqual(res['Score'][3], 15)
        self.assertEqual(res['Score'][4], 15)

        inp = {
            "weight": 5
        }
        res = self.np.calculate_score(inp)
        self.assertEqual(res['Score'][0], 25)
        self.assertEqual(res['Score'][1], 25)
        self.assertEqual(res['Score'][2], 25)
        self.assertEqual(res['Score'][3], 25)
        self.assertEqual(res['Score'][4], 25)

        inp = {
            "weight": 6
        }
        self.assertRaises(ValueError, self.np.calculate_score, inp)

        inp = {
            "weight": 0
        }
        self.assertRaises(ValueError, self.np.calculate_score, inp)

        inp = {
            "weight": -1
        }
        self.assertRaises(ValueError, self.np.calculate_score, inp)


if __name__ == '__main__':
    unittest.main()