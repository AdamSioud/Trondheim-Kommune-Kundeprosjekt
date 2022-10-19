from server.model.src.parameters.environment_param_interface import EnvironmentParam


class WellBeingParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'trivsel')
        self.INPUT_NAME = 'well_being_input'

'''
# Testing ...
well_being_input = {
    'weight' : 4
}

data = Data();
wbp = WellBeingParam(data)
print(wbp.calculate_score(well_being_input).head())'''