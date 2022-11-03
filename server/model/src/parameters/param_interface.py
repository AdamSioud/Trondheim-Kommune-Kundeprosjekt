from server.model.src.data.data import Data
from abc import ABC, abstractmethod
import pandas as pd


class ParamInterface(ABC):
    """Abstract class for parameters"""
    def __init__(self, data: Data):
        self.data = data

    @abstractmethod
    def give_score(self, *args) -> int:
        """Gives a score from 0-5 for a single zone"""
        pass

    @staticmethod
    def validate_weight(inp: dict) -> None:
        """Raises an error if the 'weight'-input is not valid."""
        weight = inp['weight']
        if weight < 1 or weight > 5:
            raise ValueError(f"'weight' needs to be between 1 and 5, was {weight}")

    @staticmethod
    def validate_args(inp: dict, args: list) -> None:
        """Raises an error if the input does not match the desired arguments"""
        if len(inp) != len(args):
            raise ValueError(f"expected {len(args)} arguments, was: {len(inp)}")
        for arg in args:
            if arg not in inp.keys():
                raise ValueError(f"input must contain {args}, did contain:  {inp.keys()}")

    @abstractmethod
    def validate_input(self, inp: dict) -> None:
        """Raises an error of the input is not valid."""
        pass

    def make_df_copy(self, key: str) -> pd.DataFrame:
        """Makes a copy of the DataFrame with the given key."""
        return self.data.DFS.get(key).copy()

    @abstractmethod
    def calculate_score(self, inp: dict) -> pd.DataFrame:
        """Calculates the score for all the zones, using give_score on each."""
        pass
