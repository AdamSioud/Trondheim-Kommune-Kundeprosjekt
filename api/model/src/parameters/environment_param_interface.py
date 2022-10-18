from api.model.src.parameters.param_interface import ParamInterface


class EnvironmentParam(ParamInterface):
    """Abstract"""

    def __init__(self, data, category):
        super().__init__(data)
        self.INPUT_NAME = ''
        self.category = category
        self.interval = self.getInterval()

    def getInterval(self):
        """
        Adding Erlends code here
        """
        inter = self.data.INTERVAL_DFS.get('Nærmiljø')[self.category + '.intervall'][1:]
        intervalList = []
        for i in range(1, len(inter) + 1):
            intervalList.append(inter.get(i) * 0.01)
        return intervalList

    def give_score(self, x):
        """
        Returns the score given by Trondheim Kommune
        """
        for i in range(4):
            if x < self.interval[i]:
                return i + 1
        return 5

    def calculate_score(self, input_: dict):
        """
        Insert description here
        """
        result = self.data.DFS.get('Nærmiljø').copy()
        result['Score-kvinner'] = result[self.category + '-kvinner.Andel'].apply(lambda x: self.give_score(x))
        result['Score-menn'] = result[self.category + '-menn.Andel'].apply(lambda x: self.give_score(x))

        clms = ['Score-menn', 'Score-kvinner']
        result['Score'] = result[clms].sum(axis=1).apply(lambda x: x / 2)
        return result.filter(
            items=['Levekårsnavn', self.category + '-kvinner.Andel', self.category + '-menn.Andel', 'Score-kvinner',
                   'Score-menn', 'Score'])