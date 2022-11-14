import pandas as pd
from server.model.src.data.data import Data
from server.model.src.parameters.param_interface import ParamInterface


class PriceParam(ParamInterface):
    """Class for calculating score for price-parameter"""
    def __init__(self):
        super().__init__()
        self.INPUT_NAME = "price_input"

    def give_score(self, price: float, budget: float, deviation=0.10) -> int:
        """
        calculates the score from 0-5 for a price is within budget .
        * 5: within budget.
        * 4-1: is distributed evenly within 10% over budget
        * 0: more than 10% over budget
        :param price: The price for the zone.
        :param budget: The budget.
        :param deviation: The deviation from the budget that should give a score > 0.
        """
        min_ = 0
        max_ = budget
        for p in range(5, 0, -1):
            if min_ < price <= max_:
                return p
            min_ = max_
            max_ += budget * deviation / 4
        return 0

    def validate_input(self, inp: dict) -> None:
        self.validate_args(inp, ['budget', 'weight'])
        self.validate_weight(inp)
        budget = inp['budget']
        if budget < 0:
            raise ValueError(f"'budget' needs to be more than 0, was {budget}")

    def calculate_score(self, inp: dict) -> pd.DataFrame:
        """
        Calculates the score for all the zones, using give_score on each zone.
        :param inp: The input on format: 'price_input' = { 'budget': int, 'weight': int }
        :return: Dataframe with the score.
        """
        self.validate_input(inp)
        result = self.make_df_copy('price')
        budget = inp['budget']
        weight = inp['weight']
        clm = 'average.averagePrice'
        result['score'] = result[clm].apply(lambda price: self.give_score(price, budget) * weight)
        return result.filter(items=['score'])
