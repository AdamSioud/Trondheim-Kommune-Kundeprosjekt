from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter
from server.model.src.parameters.abstract_parameter import AbstractParameter


class NoiseTrafficParameter(AbstractNeighborhoodParameter):

    def __init__(self):
        super().__init__('noiseTraffic')
        self.INPUT_NAME = 'noise_traffic_input'

    def give_score(self, x):
        """
        Returns the score given by Trondheim Kommune
        """
        for i in range(4):
            if x < self.interval[i]:
                return 5 - i
        return 1


class NoiseOtherParameter(AbstractNeighborhoodParameter):

    def __init__(self):
        super().__init__('noiseOther')
        self.INPUT_NAME = 'noise_other_input'

    def give_score(self, x):
        """
        Returns the score given by Trondheim Kommune
        """
        for i in range(4):
            if x < self.interval[i]:
                return 5 - i
        return 1


class NoiseParameter(AbstractParameter):

    def __init__(self):
        super().__init__()
        self.INPUT_NAME = 'noise_input'

    def validate_input(self, inp: dict) -> None:
        pass

    def give_score(self, *args):
        pass

    def calculate_score(self, input_):
        result = (NoiseTrafficParameter().calculate_score(input_) + NoiseOtherParameter().calculate_score(input_)) / 2
        return result.filter(items=['score'])
