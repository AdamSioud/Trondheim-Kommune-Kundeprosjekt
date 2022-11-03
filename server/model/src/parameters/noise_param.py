from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.parameters.param_interface import ParamInterface
from server.model.src.data.data import Data


class NoiseTrafficParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'noiseTraffic')
        self.INPUT_NAME = 'noise_traffic_input'

    def give_score(self, x):
        """
        Returns the score given by Trondheim Kommune
        """
        for i in range(4):
            if x < self.interval[i]:
                return 5 - i
        return 1


class NoiseOtherParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'noiseOther')
        self.INPUT_NAME = 'noise_other_input'

    def give_score(self, x):
        """
        Returns the score given by Trondheim Kommune
        """
        for i in range(4):
            if x < self.interval[i]:
                return 5 - i
        return 1


class NoiseParam(ParamInterface):

    def __init__(self, data):
        super().__init__(data)
        self.INPUT_NAME = 'noise_input'

    def validate_input(self, inp: dict) -> None:
        pass

    def give_score(self, *args):
        pass

    def calculate_score(self, input_):
        result = (NoiseTrafficParam(self.data).calculate_score(input_) + NoiseOtherParam(self.data).calculate_score(input_)) / 2
        return result.filter(items=['score'])
