from api.model.src.parameters.SliderParam import SliderParam


class PriceSliderParam(SliderParam):

    def __init__(self, data, min_val: float, max_val: float):
        super().__init__(data, min_val, max_val)
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
        for sel in input_['selected']:
            clm = sel + '.Gjennomsnittspris'
            score_clm = 'Score-' + sel
            score_coulmns.append(score_clm)
            result['Score-' + sel] = result[clm].apply(lambda price: self.__give_score(price, budget))
        result['Score'] = result[score_coulmns].max(axis=1)
        return result.filter(items=['Levekårsnavn', 'Score'])


'''
# testing...
data = Data()

price_slider = PriceSliderParam(data, 0.0, 3000000.0)
price_input = {
    "selected": ['small', "medium"],
    "budget": 2600000
}

print(price_slider.calculate_score(price_input).head())
'''

