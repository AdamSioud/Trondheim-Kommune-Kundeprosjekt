from server.model.src.parameters.environment_param_interface import EnvironmentParam


class TransportParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'publicTransport')
        self.INPUT_NAME = 'transport_input'
