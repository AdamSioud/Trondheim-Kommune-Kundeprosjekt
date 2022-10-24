import unittest
from server.model.src.parameters.safety_param import SafetyParam
from server.model.src.data.data import Data


class TestSafetyParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.sp = SafetyParam(self.data)
        self.input = {
            'weight': 0.5
        }

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
        self.sp.calculate_score(self.input)
        # Need to put in weighting before testing
        pass


if __name__ == '__main__':
    unittest.main()
