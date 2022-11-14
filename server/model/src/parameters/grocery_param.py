from server.model.src.parameters.environment_param_interface import EnvironmentParam
from server.model.src.data.data import Data


class GroceryParam(EnvironmentParam):
    """Class for calculating score for grocery param. The data tells portion of the inhabitants that are satisfied with
    the grocery stores, restaurants and other service offers in the area.
    """
    def __init__(self):
        super().__init__('groceryStores')
        self.INPUT_NAME = 'grocery_input'
