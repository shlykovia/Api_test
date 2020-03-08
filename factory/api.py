from abc import ABC, abstractmethod

"""It is api factory"""


class Api(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def get(self):
        return None
