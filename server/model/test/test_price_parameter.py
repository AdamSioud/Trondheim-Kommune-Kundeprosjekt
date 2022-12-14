import unittest
from unittest.mock import MagicMock
from server.model.src.parameters.price_parameter import PriceParameter
from server.model.src.data.data_manager import DataManager
import pandas as pd


class TestPriceParameter(unittest.TestCase):

    def setUp(self) -> None:
        self.pp = PriceParameter()
        PriceParameter.make_df_copy = MagicMock()
        PriceParameter.make_df_copy.return_value = pd.read_json('mock_data/price.json')

    def test_give_score(self):
        # TODO: add edge-cases. negative
        self.assertEqual(self.pp.give_score(100, 100), 5)
        self.assertEqual(self.pp.give_score(101, 100), 4)
        self.assertEqual(self.pp.give_score(102.5, 100), 4)
        self.assertEqual(self.pp.give_score(103, 100), 3)
        self.assertEqual(self.pp.give_score(105, 100), 3)
        self.assertEqual(self.pp.give_score(107, 100), 2)
        self.assertEqual(self.pp.give_score(107.5, 100), 2)
        self.assertEqual(self.pp.give_score(108, 100), 1)
        self.assertEqual(self.pp.give_score(110, 100), 1)
        self.assertEqual(self.pp.give_score(111, 100), 0)

    def test_calculate_score(self):
        inp = {
            "budget": 3600000,
            'weight': 1
        }
        res = self.pp.calculate_score(inp)
        self.assertEqual(res['score'][0], 5)
        self.assertEqual(res['score'][1], 0)
        self.assertEqual(res['score'][2], 5)
        self.assertEqual(res['score'][3], 3)
        self.assertEqual(res['score'][4], 0)

        inp = {
            "budget": 7000000,
            'weight': 2
        }
        res = self.pp.calculate_score(inp)
        self.assertEqual(res['score'][0], 10)
        self.assertEqual(res['score'][1], 10)
        self.assertEqual(res['score'][2], 10)
        self.assertEqual(res['score'][3], 10)
        self.assertEqual(res['score'][4], 2)

        inp = {
            "budget": 3600000,
            'weight': 0
        }
        self.assertRaises(ValueError, self.pp.calculate_score, inp)

        inp = {
            "budget": 3600000,
            'weight': 6
        }
        self.assertRaises(ValueError, self.pp.calculate_score, inp)

        inp = {
            "budget": 3600000,
            'weight': 6,
            "notAnInput": 2
        }
        self.assertRaises(ValueError, self.pp.calculate_score, inp)




if __name__ == '__main__':
    unittest.main()
