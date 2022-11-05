from abc import ABC, abstractmethod


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(files):
        raise NotImplementedError
