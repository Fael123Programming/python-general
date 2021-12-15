from abc import ABC, abstractmethod
from sys import platform

class Button(ABC):  # This is an interface!
    @abstractmethod
    def paint(self):
        pass

