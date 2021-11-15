from abc import ABC, abstractmethod


class Convert(ABC):
    @abstractmethod
    def convert_to_obj(self, json_string):
        pass

