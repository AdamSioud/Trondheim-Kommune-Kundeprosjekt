from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


class WellBeingParam(EnvironmentParam):
    """Class for calculating score for well-being param. The data tells the portion of the inhabitants that enjoy living
    in the area.
    """
    def __init__(self):
        super().__init__('wellBeing')
        self.INPUT_NAME = 'well_being_input'
