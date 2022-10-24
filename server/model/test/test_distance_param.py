import unittest

from shapely.speedups._speedups import Point

from server.model.src.parameters.distance_param import DistanceParam
from server.model.src.data.data import Data


class TestDistanceParam(unittest.TestCase):

    def setUp(self) -> None:
        self.data = Data()
        self.dp = DistanceParam(self.data)
        self.input = {
            "posistion": Point(10.39628304564158, 63.433247153410214)
        }

    def test_give_score(self):
        position = Point(10.39628304564158, 63.433247153410214)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 1)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 1)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 2)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 2)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 3)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 3)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 4)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 4)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 5)

        multi_polygon = self.data.GEOMETRY[0]
        self.assertEqual(self.dp.give_score(multi_polygon, position), 5)

    def test_calculate_score(self):
        self.dp.calculate_score(self.input)
        # Need to put in weighting before testing
        pass


if __name__ == '__main__':
    unittest.main()
