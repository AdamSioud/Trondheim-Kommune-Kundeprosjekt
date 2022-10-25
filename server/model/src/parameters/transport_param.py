from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


class TransportParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet offentlig transport')
        self.INPUT_NAME = 'transport_input'



# # Testing ...
# d = Data()
# transport_input = {
#     'weight' : 2
# }
#
# tp = TransportParam(d)
# print(tp.calculate_score(transport_input).head())
