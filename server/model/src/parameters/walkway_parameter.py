from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter


class WalkwayParameter(AbstractNeighborhoodParameter):
    """Class for calculating score for walkway param. The data tells the portion of the inhabitants that are satisfied
    with the walkways and bike paths in the area.
    """
    def __init__(self):
        super().__init__('walkwayAndBikePath')
        self.INPUT_NAME = 'walkway_input'
