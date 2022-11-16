from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter


class WellBeingParameter(AbstractNeighborhoodParameter):
    """Class for calculating score for well-being param. The data tells the portion of the inhabitants that enjoy living
    in the area.
    """
    def __init__(self):
        super().__init__('wellBeing')
        self.INPUT_NAME = 'well_being_input'
