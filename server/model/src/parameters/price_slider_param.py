from server.model.src.parameters.slider_param import SliderParam
from server.model.src.data.data import Data


class PriceSliderParam(SliderParam):

    def __init__(self, data):
        super().__init__(data)
        self.INPUT_NAME = "price_input"

    def __give_score(self, price, budget) -> int:
        return super()._give_score(price, budget, True)

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
            result['Score-' + sel] = result[clm].apply(lambda price: self.__give_score(price, budget) * weight)
        result['Score'] = result[score_coulmns].max(axis=1)
        return result.filter(items=['Levekårsnavn', 'Score'])



# # testing...
# data = Data()
#
# price_slider = PriceSliderParam(data)
# price_input = {
#     "selected": ['small', "medium"],
#     "budget": 2600000,
#     'weight': 4
# }
#
# print(price_slider.calculate_score(price_input).head())
