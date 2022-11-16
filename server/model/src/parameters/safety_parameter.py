from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter


class SafetyParameter(AbstractNeighborhoodParameter):
    """Class for calculating score for safety param. The data tells portion of the inhabitants that feels safe in the
    area.
    """
    def __init__(self):
        super().__init__('safety')
        self.INPUT_NAME = 'safety_input'
