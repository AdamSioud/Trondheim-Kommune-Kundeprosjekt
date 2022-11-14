from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


class CultureParam(EnvironmentParam):
    """Class for calculating score for culture param. The data tells portion of the inhabitants that are satisfied with
    the culture and sport facilities in the area.
    """
    def __init__(self):
        super().__init__('culture')
        self.INPUT_NAME = 'culture_input'
