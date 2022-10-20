import unittest
from server.model.src.parameters.age_param import AgeParam
from server.model.src.data.data import Data


class TestAgeParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.ap = AgeParam(self.data)

    def test_give_score(self):
        self.assertEqual(self.ap._AgeParam__give_score(101, 100), 5)
        self.assertEqual(self.ap._AgeParam__give_score(100, 100), 5)
        self.assertEqual(self.ap._AgeParam__give_score(99, 100), 4)
        self.assertEqual(self.ap._AgeParam__give_score(97.5, 100), 4)
        self.assertEqual(self.ap._AgeParam__give_score(97, 100), 3)
        self.assertEqual(self.ap._AgeParam__give_score(95, 100), 3)
        self.assertEqual(self.ap._AgeParam__give_score(93, 100), 2)
        self.assertEqual(self.ap._AgeParam__give_score(92.5, 100), 2)
        self.assertEqual(self.ap._AgeParam__give_score(92, 100), 1)
        self.assertEqual(self.ap._AgeParam__give_score(90, 100), 1)
        self.assertEqual(self.ap._AgeParam__give_score(89, 100), 0)


if __name__ == '__main__':
    unittest.main()
