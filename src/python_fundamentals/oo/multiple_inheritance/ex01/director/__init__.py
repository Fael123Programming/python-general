from src.python_fundamentals.oo.multiple_inheritance.ex01.functionary import Functionary
from src.python_fundamentals.oo.multiple_inheritance.ex01.authenticable import Authenticable


class Director(Functionary, Authenticable):

    def __init__(self, name, cpf, address, salary, department):
        super().__init__(name, cpf, address, salary)
        self._department = department

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    def get_bonus(self, tax):
        return super().get_bonus(tax) + 1200

    def authenticate(self):
        # Do some logic check...
        pass
