from src.python_fundamentals.oo.multiple_inheritance.ex01.functionary import Functionary
from src.python_fundamentals.oo.multiple_inheritance.ex01.authenticable import Authenticable


class Manager(Functionary, Authenticable):
    def __init__(self, name, cpf, address, salary):
        super().__init__(name, cpf, address, salary)
        self._subordinates = list()

    @property
    def subordinates(self):
        return self._subordinates

    def add_subordinate(self, subordinate):
        if not isinstance(subordinate, Functionary):
            raise ValueError("subordinate is not a functionary")
        self._subordinates.append(subordinate)

    def get_bonus(self, tax):
        return super().get_bonus(tax) + 1000

    def authenticate(self):
        pass
