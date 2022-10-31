from server.model.src.parameters.param_interface import ParamInterface


class AgeParam(ParamInterface):

    def __init__(self, data):
        super().__init__(data)
        self.INPUT_NAME = "age_input"

    def give_score(self, price: float, budget: float, deviation=0.10) -> int:
        """
        calculates the score from 0-5 for if a price is within budget .
        * 5: within budget.
        * 4-1: is distributed evenly within 10% over budget
        * 0: more than 10% over budget
        """
        min_ = budget
        max_ = float('inf')
        for p in range(5, 0, -1):
            if min_ <= price < max_:
                return p
            max_ = min_
            min_ -= budget * deviation / 4
        return 0

    def validate_input(self, input_):
        self.validate_args(input_, ['selected', 'percent', 'weight'])
        self.validate_weight(input_)
        if len(input_['selected']) == 0:
            raise ValueError(f"'selected' can´t be empty")
        percent = input_['percent']
        if percent < 0 or percent > 100:
            raise ValueError(f"'percent' needs to be between 0 and 100, was {percent}")

    def calculate_score(self, input_: dict):
        self.validate_input(input_)
        result = self.make_df_copy('Ages')
        percent = input_['percent'] / 100
        clms = []
        for sel in input_['selected']:
            clms.append(sel + ".Andel")
        weight = input_['weight']
        # should .round(2) be here. result becomes different ... ??
        result['Score'] = result[clms].sum(axis=1).round(2)\
            .apply(lambda price: self.give_score(price, percent) * weight)
        return result.filter(items=['Levekårsnavn', 'Score'])
