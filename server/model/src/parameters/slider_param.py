from server.model.src.parameters.param_interface import ParamInterface
from abc import abstractmethod


class SliderParam(ParamInterface):

    def __init__(self, data):
        super().__init__(data)

    def _give_score(self, price: float, budget: float, maximum_slider: bool, deviation=0.10) -> int:
        """
        calculates the score from 0-5 for if a price is within budget .
        * 5: within budget.
        * 4-1: is distributed evenly within 10% over budget
        * 0: more than 10% over budget
        """
        if maximum_slider:
            min_ = 0
            max_ = budget
        else:
            min_ = budget
            max_ = float('inf')
        for p in range(5, 0, -1):
            if min_ < price <= max_:
                return p
            if maximum_slider:
                min_ = max_
                max_ += budget * deviation / 4
            else:
                max_ = min_
                min_ -= budget * deviation / 4
        return 0

    @abstractmethod
    def calculate_score(self):
        pass
