from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


class SafetyParam(EnvironmentParam):
    """Class for calculating score for safety param. The data tells portion of the inhabitants that feels safe in the
    area.
    """
    def __init__(self):
        super().__init__('safety')
        self.INPUT_NAME = 'safety_input'
