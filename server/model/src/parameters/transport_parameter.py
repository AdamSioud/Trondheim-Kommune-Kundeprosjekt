from server.model.src.parameters.abstract_neighborhood_parameter import AbstractNeighborhoodParameter


class TransportParameter(AbstractNeighborhoodParameter):
    """Class for calculating score for transport param. The data tells the portion of the inhabitants that are satisfied
    with the availability of public transport in the area.
    """
    def __init__(self):
        super().__init__('publicTransport')
        self.INPUT_NAME = 'transport_input'
