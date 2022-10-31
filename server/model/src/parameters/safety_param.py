from server.model.src.parameters.environment_param_interface import EnvironmentParam


class SafetyParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'trygghet')
        self.INPUT_NAME = 'safety_input'
