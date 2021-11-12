from abc import ABC, abstractmethod


class Loading(ABC):
    @abstractmethod
    def loading_to_DWH(self, list_for_load):
        pass
