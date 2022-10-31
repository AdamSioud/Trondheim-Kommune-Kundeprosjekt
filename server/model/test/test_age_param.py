import unittest
from unittest.mock import MagicMock
from server.model.src.parameters.age_param import AgeParam
from server.model.src.data.data import Data
import pandas as pd
import unittest
from unittest.mock import MagicMock
from server.model.src.parameters.age_param import AgeParam
from server.model.src.data.data import Data
import pandas as pd


class TestAgeParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.ap = AgeParam(self.data)
        AgeParam.make_df_copy = MagicMock()
        AgeParam.make_df_copy.return_value = pd.read_json('mock_data/ages.json')

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
            "selected": ['underage (0-17)', 'young adult (18-34)'],
            "percent": 50,
            "weight": 1
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 5)
        self.assertEqual(res['Score'][1], 1)
        self.assertEqual(res['Score'][2], 5)
        self.assertEqual(res['Score'][3], 5)
        self.assertEqual(res['Score'][4], 5)

        inp = {
            "selected": ['underage (0-17)', 'young adult (18-34)'],
            "percent": 50,
            "weight": 2
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 10)
        self.assertEqual(res['Score'][1], 2)
        self.assertEqual(res['Score'][2], 10)
        self.assertEqual(res['Score'][3], 10)
        self.assertEqual(res['Score'][4], 10)

        inp = {
            "selected": ['underage (0-17)', 'young adult (18-34)'],
            "percent": 0,
            "weight": 2
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 10)
        self.assertEqual(res['Score'][1], 10)
        self.assertEqual(res['Score'][2], 10)
        self.assertEqual(res['Score'][3], 10)
        self.assertEqual(res['Score'][4], 10)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 12,
            "weight": 1
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 1)
        self.assertEqual(res['Score'][1], 5)
        self.assertEqual(res['Score'][2], 0)
        self.assertEqual(res['Score'][3], 5)
        self.assertEqual(res['Score'][4], 5)

        inp = {
            "selected": [],
            "percent": 12,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": -1,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 101,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 7,
            "weight": 6
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 10,
            "weight": 0
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 10,
            "weight": 1,
            "notAnInput": 2
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)


if __name__ == '__main__':
    unittest.main()


class TestAgeParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.ap = AgeParam(self.data)
        AgeParam.make_df_copy = MagicMock()
        AgeParam.make_df_copy.return_value = pd.read_json('mock_data/ages.json')

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
            "selected": ['underage (0-17)', 'young adult (18-34)'],
            "percent": 50,
            "weight": 1
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 5)
        self.assertEqual(res['Score'][1], 1)
        self.assertEqual(res['Score'][2], 5)
        self.assertEqual(res['Score'][3], 5)
        self.assertEqual(res['Score'][4], 5)

        inp = {
            "selected": ['underage (0-17)', 'young adult (18-34)'],
            "percent": 50,
            "weight": 2
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 10)
        self.assertEqual(res['Score'][1], 2)
        self.assertEqual(res['Score'][2], 10)
        self.assertEqual(res['Score'][3], 10)
        self.assertEqual(res['Score'][4], 10)

        inp = {
            "selected": ['underage (0-17)', 'young adult (18-34)'],
            "percent": 0,
            "weight": 2
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 10)
        self.assertEqual(res['Score'][1], 10)
        self.assertEqual(res['Score'][2], 10)
        self.assertEqual(res['Score'][3], 10)
        self.assertEqual(res['Score'][4], 10)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 12,
            "weight": 1
        }
        res = self.ap.calculate_score(inp)
        self.assertEqual(res['Score'][0], 1)
        self.assertEqual(res['Score'][1], 5)
        self.assertEqual(res['Score'][2], 0)
        self.assertEqual(res['Score'][3], 5)
        self.assertEqual(res['Score'][4], 5)

        inp = {
            "selected": [],
            "percent": 12,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": -1,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 101,
            "weight": 1
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 7,
            "weight": 6
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 10,
            "weight": 0
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)

        inp = {
            "selected": ['underage (0-17)'],
            "percent": 10,
            "weight": 1,
            "notAnInput": 2
        }
        self.assertRaises(ValueError, self.ap.calculate_score, inp)


if __name__ == '__main__':
    unittest.main()
