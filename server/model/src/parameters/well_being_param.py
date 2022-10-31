from server.model.src.parameters.environment_param_interface import EnvironmentParam


class WellBeingParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'trivsel')
        self.INPUT_NAME = 'well_being_input'
