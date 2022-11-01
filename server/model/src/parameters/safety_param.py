from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data

class SafetyParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'safety')
        self.INPUT_NAME = 'safety_input'

# d = Data()
# p = SafetyParam(d)
# safety_input = {
#     'weight': 1
# }
#
# print(p.calculate_score(safety_input))