from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter


class CultureParameter(AbstractNeighborhoodParameter):
    """Class for calculating score for culture param. The data tells portion of the inhabitants that are satisfied with
    the culture and sport facilities in the area.
    """
    def __init__(self):
        super().__init__('culture')
        self.INPUT_NAME = 'culture_input'
