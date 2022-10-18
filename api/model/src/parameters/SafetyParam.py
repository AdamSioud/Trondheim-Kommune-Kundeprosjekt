from api.model.src.parameters.EnvironmentParamInterface import EnvironmentParam


class SafetyParam(EnvironmentParam):


    def __init__(self, data):
        super().__init__(data, 'trygghet')
        self.INPUT_NAME = 'safety_input'

'''
# Testing ...
data = Data()

safety_input = {
    'weight' : 4
}

sp = SafetyParam(data)
print(sp.calculate_score(safety_input).head())
'''
