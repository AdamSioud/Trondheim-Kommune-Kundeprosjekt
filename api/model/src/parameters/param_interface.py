from abc import ABC, abstractmethod


class ParamInterface(ABC):

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def calculate_score(self):
        pass
