from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


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
print(sp.get_interval())
'''

# resu = data.DFS.get('Nærmiljø').copy()
# with open("nærmiljø.json", "w") as outfile:
#     outfile.write(resu.head().to_json())


