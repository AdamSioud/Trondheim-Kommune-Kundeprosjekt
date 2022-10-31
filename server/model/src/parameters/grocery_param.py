from server.model.src.parameters.environment_param_interface import EnvironmentParam


class GroceryParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet butikker')
        self.INPUT_NAME = 'grocery_input'
