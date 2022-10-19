from api.model.src.parameters.environment_param_interface import EnvironmentParam


class GroceryParam(EnvironmentParam):

    def __init__(self, data):
        super().__init__(data, 'tilgjengelighet butikker')
        self.INPUT_NAME = 'grocery_input'

'''
# Testing ...

grocery_input = {
    'weight' : 4
}
d = Data()
gp = GroceryParam(d)
print(gp.calculate_score(grocery_input).head())
'''
