from api.model.src.parameters.environment_param_interface import EnvironmentParam


class CultureParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet kultur')
        self.INPUT_NAME = 'culture_input'

'''
# Testing ...
data = Data()
culture_input = {
    'weight' : 4
}

cp = CultureParam(data)
print(cp.calculate_score(culture_input).head())
'''
