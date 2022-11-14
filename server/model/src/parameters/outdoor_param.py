from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


class OutdoorParam(EnvironmentParam):
    """Class for calculating score for outdoor param. The data tells portion of the inhabitants that are satisfied with
    the availability of nature and outdoor areas in the area.
    """
    def __init__(self):
        super().__init__('outdoorLife')
        self.INPUT_NAME = 'outdoor_input'
