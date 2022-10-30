from abc import ABC, abstractmethod


class ParamInterface(ABC):

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def give_score(self, *args):
        pass

    def make_df_copy(self, name: str):
        return self.data.DFS.get(name).copy()

    @abstractmethod
    def calculate_score(self, inp: dict):
        pass
