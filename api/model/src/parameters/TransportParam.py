from api.model.src.parameters.EnvironmentParamInterface import EnvironmentParam


class TransportParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet offentlig transport')
        self.INPUT_NAME = 'transport_input'


'''
# Testing ...
d = Data()
transport_input = {
    'weight' : 4
}

tp = TransportParam(d)
print(tp.calculate_score(transport_input).head())
'''