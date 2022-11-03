from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


class WalkwayParam(EnvironmentParam):
    """Class for calculating score for walkway param. The data tells the portion of the inhabitants that are satisfied
    with the walkways and bike paths in the area.
    """
    def __init__(self, data: Data):
        super().__init__(data, 'walkwayAndBikePath')
        self.INPUT_NAME = 'walkway_input'
