import pandas as pd
from server.model.src.parameters.param_interface import ParamInterface
from server.model.src.data.data import Data


class AgeParam(ParamInterface):
    """Class for calculating score for age-parameter"""
    def __init__(self, data: Data):
        super().__init__(data)
        self.INPUT_NAME = "age_input"

    def give_score(self, price: float, budget: float, deviation=0.10) -> int:
        """
        Gives a score from 0-5 for if a price is within budget:
            * 5: if price is within budget.
            * 4-1: is distributed evenly within 10% over budget
            * 0: more than 10% over budget
        :param price: The actual price.
        :param budget: The budget.
        :param deviation: the deviation from budget that should give a score.
        :return: The score
        """
        min_val = budget
        max_val = float('inf')
        for p in range(5, 0, -1):
            if min_val <= price < max_val:
                return p
            max_val = min_val
            min_val -= budget * deviation / 4
        return 0

    def validate_input(self, inp: dict) -> None:
        self.validate_args(inp, ['selected', 'percent', 'weight'])
        self.validate_weight(inp)
        percent = inp['percent']
        if percent < 0 or percent > 100:
            raise ValueError(f"'percent' needs to be between 0 and 100, was {percent}")

    def calculate_score(self, inp: dict) -> pd.DataFrame:
        """Calculates the score for all the zones, using give_score on each zone. Then multiplies it with the
        'weight'-input.
        :param inp: The input on format: 'age_input' = { 'selected1: [], 'percent': int, 'weight': int }
        :return: DataFrame with the score.
        """
        self.validate_input(inp)
        result = self.make_df_copy('age')
        percent = inp['percent'] / 100
        clms = []
        for sel in inp['selected']:
            clms.append(sel + ".portion")
        weight = inp['weight']
        # should .round(2) be here. result becomes different ... ??
        result['score'] = result[clms].sum(axis=1).round(2)\
            .apply(lambda price: self.give_score(price, percent) * weight)
        return result.filter(items=['score'])
