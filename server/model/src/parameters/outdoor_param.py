from server.model.src.parameters.environment_param_interface import EnvironmentParam


class OutdoorParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet friluftsområder')
        self.INPUT_NAME = 'outdoor_input'
