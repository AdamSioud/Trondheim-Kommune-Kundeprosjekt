import unittest
from unittest.mock import MagicMock
from server.model.src.parameters.age_parameter import AgeParameter
from server.model.src.data.data_manager import DataManager
import pandas as pd


class TestAgeParameter(unittest.TestCase):

    def setUp(self) -> None:
        self.ap = AgeParameter()
        AgeParameter.make_df_copy = MagicMock()
        AgeParameter.make_df_copy.return_value = pd.read_json('mock_data/age.json')

    def test_give_score(self):
        self.assertEqual(self.ap.give_score(100, 100), 5)
        self.assertEqual(self.ap.give_score(99, 100), 4)
        self.assertEqual(self.ap.give_score(97.5, 100), 4)
        self.assertEqual(self.ap.give_score(97, 100), 3)
        self.assertEqual(self.ap.give_score(95, 100), 3)
        self.assertEqual(self.ap.give_score(93, 100), 2)
        self.assertEqual(self.ap.give_score(92.5, 100), 2)
        self.assertEqual(self.ap.give_score(92, 100), 1)
        self.assertEqual(self.ap.give_score(90, 100), 1)
        self.assertEqual(self.ap.give_score(89, 100), 0)

    def test_test(self):
        inp = {
            "selected": ['0-17', '18-34'],
            "percent": 50,
            "weight": 1
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['score'][0], 5)
        self.assertEqual(res['score'][1], 1)
        self.assertEqual(res['score'][2], 5)
        self.assertEqual(res['score'][3], 5)
        self.assertEqual(res['score'][4], 5)

        inp = {
            "selected": ['0-17', '18-34'],
            "percent": 50,
            "weight": 2
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['score'][0], 10)
        self.assertEqual(res['score'][1], 2)
        self.assertEqual(res['score'][2], 10)
        self.assertEqual(res['score'][3], 10)
        self.assertEqual(res['score'][4], 10)
        inp = {
            "selected": ['0-17', '18-34'],
            "percent": 0,
            "weight": 2
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['score'][0], 10)
        self.assertEqual(res['score'][1], 10)
        self.assertEqual(res['score'][2], 10)
        self.assertEqual(res['score'][3], 10)
        self.assertEqual(res['score'][4], 10)

        inp = {
            "selected": ['0-17'],
            "percent": 12,
            "weight": 1
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['score'][0], 1)
        self.assertEqual(res['score'][1], 5)
        self.assertEqual(res['score'][2], 0)
        self.assertEqual(res['score'][3], 5)
        self.assertEqual(res['score'][4], 5)

        inp = {
            "selected": ['0-17'],
            "percent": -1,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['0-17'],
            "percent": 101,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['0-17'],
            "percent": 7,
            "weight": 6
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['0-17'],
            "percent": 10,
            "weight": 0
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['0-17'],
            "percent": 10,
            "weight": 1,
            "notAnInput": 2
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)


if __name__ == '__main__':
    unittest.main()

