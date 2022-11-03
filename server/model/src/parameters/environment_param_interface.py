import pandas as pd
from server.model.src.parameters.param_interface import ParamInterface
from server.model.src.data.data import Data


class EnvironmentParam(ParamInterface):
    """Abstract class for calculating score for an environment-parameter"""
    def __init__(self, data: Data, category: str):
        super().__init__(data)
        self.category = category
        self.dataColumn = 'portion'
        self.interval = self.get_interval()

    def get_interval(self) -> list:
        """Returns the correct interval from data_interval.json"""
        inter = self.data.INTERVAL_DFS.get('neighborhood')[self.category + '.interval'][1:]
        interval_list = []
        for i in range(1, len(inter) + 1):
            interval_list.append(inter.get(i) * 0.01)
        return interval_list

    def give_score(self, x: float) -> int:
        """Gives a score from 1-5 based on the interval"""
        for i in range(4):
            if x < self.interval[i]:
                return i + 1
        return 5

    def validate_input(self, inp: dict) -> None:
        self.validate_args(inp, ['weight'])
        self.validate_weight(inp)

    def calculate_score(self, inp: dict) -> pd.DataFrame:
        """
        Calculates separately the score for men and women for each zone using give_score. Then calculates the mean value
        for each zone and multiplies it with the weight from the input.
        :param inp: The input on format: 'INPUT_NAME' = { 'weight': int }
        :return: DataFrame with the score.
        """
        self.validate_input(inp)
        result = self.make_df_copy('neighborhood')
        result['scoreW'] = result[self.category + 'W.' + self.dataColumn].apply(lambda x: self.give_score(x))
        result['scoreM'] = result[self.category + 'M.' + self.dataColumn].apply(lambda x: self.give_score(x))
        clms = ['scoreW', 'scoreM']
        weight = inp['weight']
        result['score'] = result[clms].sum(axis=1).apply(lambda x: (x / 2) * weight)
        return result.filter(items=['score'])
