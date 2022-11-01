from server.model.src.parameters.environment_param_interface import EnvironmentParam


class WalkwayParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'walkwayAndBikePath')
        self.INPUT_NAME = 'walkway_input'
