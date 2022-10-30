import unittest
from unittest.mock import MagicMock
from server.model.src.parameters.price_param import PriceParam
from server.model.src.data.data import Data
import pandas as pd


class TestPriceParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.pp = PriceParam(self.data)

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


    # def test_test(self):
    #     PriceParam.make_df_copy = MagicMock()
    #     PriceParam.make_df_copy.return_value = pd.read_json('mock_data/ages.json')
    #     inp = {}
    #
    #     res = self.pp.calculate_score(inp)
    #     self.assertEqual(res['Score'][0], 5)
    #     self.assertEqual(res['Score'][1], 1)
    #     self.assertEqual(res['Score'][2], 5)
    #     self.assertEqual(res['Score'][3], 5)
    #     self.assertEqual(res['Score'][4], 5)
    #
    #     inp = {
    #         "selected": ['underage (0-17)', 'young adult (18-34)'],
    #         "percent": 50,
    #         "weight": 2
    #     }
    #     res = self.pp.calculate_score(inp)
    #     self.assertEqual(res['Score'][0], 10)
    #     self.assertEqual(res['Score'][1], 2)
    #     self.assertEqual(res['Score'][2], 10)
    #     self.assertEqual(res['Score'][3], 10)
    #     self.assertEqual(res['Score'][4], 10)
    #
    #     inp = {
    #         "selected": ['underage (0-17)', 'young adult (18-34)'],
    #         "percent": 0,
    #         "weight": 2
    #     }
    #     res = self.pp.calculate_score(inp)
    #     self.assertEqual(res['Score'][0], 10)
    #     self.assertEqual(res['Score'][1], 10)
    #     self.assertEqual(res['Score'][2], 10)
    #     self.assertEqual(res['Score'][3], 10)
    #     self.assertEqual(res['Score'][4], 10)
    #
    #     inp = {
    #         "selected": ['underage (0-17)'],
    #         "percent": 12,
    #         "weight": 1
    #     }
    #     res = self.pp.calculate_score(inp)
    #     self.assertEqual(res['Score'][0], 1)
    #     self.assertEqual(res['Score'][1], 5)
    #     self.assertEqual(res['Score'][2], 0)
    #     self.assertEqual(res['Score'][3], 5)
    #     self.assertEqual(res['Score'][4], 5)


if __name__ == '__main__':
    unittest.main()
