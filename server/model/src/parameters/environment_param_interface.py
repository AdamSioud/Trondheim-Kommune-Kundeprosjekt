from server.model.src.parameters.param_interface import ParamInterface


class EnvironmentParam(ParamInterface):
    """Abstract"""
    def __init__(self, data, category):
        super().__init__(data)
        self.category = category
        self.dataColumn = 'portion'
        self.interval = self.get_interval()

    def get_interval(self):
        """
        Adding Erlends code here
        """
        inter = self.data.INTERVAL_DFS.get('neighborhood')[self.category + '.interval'][1:]
        interval_list = []
        for i in range(1, len(inter) + 1):
            interval_list.append(inter.get(i) * 0.01)
        return interval_list

    def give_score(self, x):
        """
        Returns the score given by Trondheim Kommune
        """
        for i in range(4):
            if x < self.interval[i]:
                return i + 1
        return 5

    def validate_input(self, input_):
        self.validate_args(input_, ['weight'])
        self.validate_weight(input_)

    def calculate_score(self, input_: dict):
        """
        Insert description here
        """
        self.validate_input(input_)
        result = self.make_df_copy('neighborhood')
        result['scoreW'] = result[self.category + 'W.' + self.dataColumn].apply(lambda x: self.give_score(x))
        result['scoreM'] = result[self.category + 'M.' + self.dataColumn].apply(lambda x: self.give_score(x))
        clms = ['scoreW', 'scoreM']
        weight = input_['weight']
        result['score'] = result[clms].sum(axis=1).apply(lambda x: (x / 2) * weight)
        return result.filter(items=['safetyW.portion','safetyM.portion', 'scoreW', 'scoreM', 'score'])
