import shapely
from shapely.geometry import Point
from server.model.src.parameters.param_interface import ParamInterface


class DistanceParam(ParamInterface):

    def __init__(self, data):
        super().__init__(data)
        self.INPUT_NAME = "distance_input"

    def give_score(self, bydel: shapely.geometry.multipolygon.MultiPolygon, pos: shapely.geometry.point.Point,
                   min_distance=0.02, increment=0.01) -> int:
        """
        Add converter? To timeconsuming, save it for later
        1 degree is approx 111.1 km
        """
        center = bydel.centroid
        distance = pos.distance(center)
        limit = min_distance

        for p in range(5, 0, -1):
            if distance <= limit:
                return p
            limit += increment
        return 0

    def make_df_copy(self):
        return self.data.add_geometry_column(self.data.GENERAL_DF)

    def validate_input(self, input_):
        for arg in ['position', 'weight']:
            if arg not in input_.keys():
                raise ValueError(f"input must contain ['position', 'weight'], did contain:  {input_.keys()}")
        weight = input_['weight']
        if weight < 1 or weight > 5:
            raise ValueError(f"'weight' needs to be between 1 and 5, was {weight}")

    def calculate_score(self, input_: dict) -> float:
        """
        Calculates the distance from centroid of an area to the coordinates of the point

        input-format:
        input_ = {
            position: POINT (10.39628304564158 63.433247153410214),
            weight: 4
        }
        """
        self.validate_input(input_)
        result = self.make_df_copy()
        pos = input_.get('position')
        weight = input_['weight']
        result['Score'] = result['geometry'].apply(lambda x: self.give_score(x, pos) * weight)
        return result.filter(items=['Levekårsnavn', 'geometry', 'Score'])

'''
distance_input = {
    "position": Point (10.39628304564158, 63.433247153410214),
    "weight": 4
}
data = Data();
ages_param = DistanceParam(data)
print(ages_param.calculate_score(distance_input).head())
'''
