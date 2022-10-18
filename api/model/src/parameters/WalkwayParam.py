from api.model.src.parameters.EnvironmentParamInterface import EnvironmentParam


class WalkwayParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet gang og sykkelvei')
        self.INPUT_NAME = 'walkway_input'
'''
# Testing ...

walkway_input = {
    'weight' : 4
}
d = Data()
wp = WalkwayParam(d)
print(wp.calculate_score(walkway_input).head())
'''
