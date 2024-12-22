print("LA: 25")
from abc import ABC, abstractmethod

class Char(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Batman(Char):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

b = Batman("Bruce Wayne", "Batman")
print(b.alias)