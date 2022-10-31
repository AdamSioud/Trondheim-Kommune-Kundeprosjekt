from abc import ABC, abstractmethod


class ParamInterface(ABC):

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def give_score(self, *args):
        pass

    def validate_weight(self, inp):
        weight = inp['weight']
        if weight < 1 or weight > 5:
            raise ValueError(f"'weight' needs to be between 1 and 5, was {weight}")

    def validate_args(self, inp, args):
        if len(inp) != len(args):
            raise ValueError(f"expected {len(args)} arguments, was: {len(inp)}")
        for arg in args:
            if arg not in inp.keys():
                raise ValueError(f"input must contain {args}, did contain:  {inp.keys()}")

    def make_df_copy(self, name: str):
        return self.data.DFS.get(name).copy()

    @abstractmethod
    def calculate_score(self, inp: dict):
        pass
