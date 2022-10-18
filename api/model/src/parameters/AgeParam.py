from api.model.src.parameters.SliderParam import SliderParam


class AgeParam(SliderParam):

    def __init__(self, data, min_val: float, max_val: float):
        super().__init__(data, min_val, max_val)
        self.INPUT_NAME = "age_input"

    def __give_score(self, price, budget):
        return super()._give_score(price, budget, False)

    def calculate_score(self, input_: dict):
        result = self.data.DFS.get('Ages').copy()
        budget = input_['percent']
        clms = []
        for sel in input_['selected']:
            clms.append(sel + ".Andel")
        # should .round(2) be here. result becomes different ... ??
        result['Score'] = result[clms].sum(axis=1).round(2).apply(lambda price: self.__give_score(price, budget))
        return result.filter(items=['Levekårsnavn', 'Score'])

'''
age_input = {
    "selected": ['underage (0-17)', 'young adult (18-34)'],
    "percent": 0.50
}
data = Data()
ages_param = AgeParam(data, 0, 100)
print(ages_param.calculate_score(age_input))
'''
