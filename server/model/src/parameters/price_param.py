from server.model.src.parameters.param_interface import ParamInterface
from server.model.src.data.data import Data


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

    def calculate_score(self, input_: dict) -> float:
        """
        Calculates the score for each value in the selected coulmns. Then stores the
        largest for each row.

        input-format:
        input_ = {
            selected: ["coulmn_1", "coulmn_2"],
            price: 12345
        }
        """
        result = self.data.DFS.get('Price').copy()
        score_coulmns = []
        budget = input_['budget']
        weight = input_['weight']
        for sel in input_['selected']:
            clm = sel + '.Gjennomsnittspris'
            score_clm = 'Score-' + sel
            score_coulmns.append(score_clm)
            result['Score-' + sel] = result[clm].apply(lambda price: self.give_score(price, budget) * weight)
        result['Score'] = result[score_coulmns].max(axis=1)
        return result.filter(items=['Levekårsnavn', 'Score'])



# # testing...
data = Data()
#
# price_slider = PriceSliderParam(data)
# price_input = {
#     "selected": ['small', "medium"],
#     "budget": 2600000,
#     'weight': 4
# }
#
# print(price_slider.calculate_score(price_input).head())

resu = data.DFS.get('Price').copy()
with open("ages.json", "w") as outfile:
    outfile.write(resu.head().to_json())