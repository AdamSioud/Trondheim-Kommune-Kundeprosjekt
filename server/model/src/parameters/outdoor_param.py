from parameters.environment_param_interface import EnvironmentParam


class OutdoorParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet friluftsområder')
        self.INPUT_NAME = 'outdoor_input'
'''
# Testing ...
data = Data()
outdoor_input = {
    'weight' : 4
}

odp = OutdoorParam(data)
print(odp.calculate_score(outdoor_input).head())
'''
