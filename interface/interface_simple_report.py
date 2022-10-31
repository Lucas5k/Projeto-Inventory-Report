from abc import ABC


class Interface_simple_report(ABC):
    @staticmethod
    def generate(list):
        raise NotImplementedError
