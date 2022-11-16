from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter


class GroceryParameter(AbstractNeighborhoodParameter):
    """Class for calculating score for grocery param. The data tells portion of the inhabitants that are satisfied with
    the grocery stores, restaurants and other service offers in the area.
    """
    def __init__(self):
        super().__init__('groceryStores')
        self.INPUT_NAME = 'grocery_input'
