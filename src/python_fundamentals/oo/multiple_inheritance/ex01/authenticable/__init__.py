from abc import ABC, abstractmethod


class Authenticable(ABC):

    @abstractmethod
    def authenticate(self) -> bool:
        pass
