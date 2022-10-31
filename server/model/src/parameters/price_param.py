from server.model.src.parameters.param_interface import ParamInterface


class PriceParam(ParamInterface):

    def __init__(self, data):
        super().__init__(data)
        self.INPUT_NAME = "price_input"

    def give_score(self, price: float, budget: float, deviation=0.10) -> int:
        """
        calculates the score from 0-5 for if a price is within budget .
        * 5: within budget.
        * 4-1: is distributed evenly within 10% over budget
        * 0: more than 10% over budget
        """
        min_ = 0
        max_ = budget
        for p in range(5, 0, -1):
            if min_ < price <= max_:
                return p
            min_ = max_
            max_ += budget * deviation / 4
        return 0

    def validate_input(self, input_):
        self.validate_args(input_, ['budget', 'weight'])
        self.validate_weight(input_)
        budget = input_['budget']
        if budget < 0:
            raise ValueError(f"'budget' needs to be more than 0, was {budget}")

    def calculate_score(self, input_: dict):
        """
        Calculates the score for each value in the selected coulmns. Then stores the
        largest for each row.

        input-format:
        input_ = {
            price: 12345
        }
        """
        self.validate_input(input_)
        result = self.make_df_copy('Price')
        budget = input_['budget']
        weight = input_['weight']
        clm = 'average.Gjennomsnittspris'
        result['Score'] = result[clm].apply(lambda price: self.give_score(price, budget) * weight)
        return result.filter(items=['Levekårsnavn', 'Score'])
