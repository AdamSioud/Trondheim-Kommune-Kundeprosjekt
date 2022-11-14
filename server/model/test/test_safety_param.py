import unittest
from server.model.src.parameters.safety_param import SafetyParam
from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data
from unittest.mock import MagicMock
import pandas as pd


class TestSafetyParam(unittest.TestCase):

    def setUp(self) -> None:
        self.sp = SafetyParam()
        # EnvironmentParam.get_interval = MagicMock()
        # EnvironmentParam.get_interval.return_value = [0.75, 0.8, 0.85, 0.9]
        SafetyParam.get_interval = MagicMock()
        SafetyParam.get_interval.return_value = [0.75, 0.8, 0.85, 0.90]
        SafetyParam.make_df_copy = MagicMock()
        SafetyParam.make_df_copy.return_value = pd.read_json('mock_data/neighborhood.json')

    def test_give_score(self):
        self.assertEqual(self.sp.give_score(0.50), 1)
        self.assertEqual(self.sp.give_score(0.749), 1)
        self.assertEqual(self.sp.give_score(0.75), 2)
        self.assertEqual(self.sp.give_score(0.799), 2)
        self.assertEqual(self.sp.give_score(0.80), 3)
        self.assertEqual(self.sp.give_score(0.849), 3)
        self.assertEqual(self.sp.give_score(0.85), 4)
        self.assertEqual(self.sp.give_score(0.899), 4)
        self.assertEqual(self.sp.give_score(0.90), 5)
        self.assertEqual(self.sp.give_score(1), 5)

    def test_calculate_score(self):
        inp = {
            "weight": 1
        }
        res = self.sp.calculate_score(inp)
        self.assertEqual(res['score'][0], 3)
        self.assertEqual(res['score'][1], 5)
        self.assertEqual(res['score'][2], 3)
        self.assertEqual(res['score'][3], 3.5)
        self.assertEqual(res['score'][4], 5)

        inp = {
            "weight": 3
        }
        res = self.sp.calculate_score(inp)
        self.assertEqual(res['score'][0], 9)
        self.assertEqual(res['score'][1], 15)
        self.assertEqual(res['score'][2], 9)
        self.assertEqual(res['score'][3], 10.5)
        self.assertEqual(res['score'][4], 15)

        inp = {
            "weight": 5
        }
        res = self.sp.calculate_score(inp)
        self.assertEqual(res['score'][0], 15)
        self.assertEqual(res['score'][1], 25)
        self.assertEqual(res['score'][2], 15)
        self.assertEqual(res['score'][3], 17.5)
        self.assertEqual(res['score'][4], 25)

        inp = {
            "weight": 6
        }
        self.assertRaises(ValueError, self.sp.calculate_score, inp)

        inp = {
            "weight": 0
        }
        self.assertRaises(ValueError, self.sp.calculate_score, inp)

        inp = {
            "weight": -1
        }
        self.assertRaises(ValueError, self.sp.calculate_score, inp)

        inp = {
            "weight": 1,
            "notAnInput": 2
        }
        self.assertRaises(ValueError, self.sp.calculate_score, inp)


if __name__ == '__main__':
    unittest.main()
