from abc import ABC, abstractmethod
from python_fundamentals.oo.inheritance.ex02.address import Address


# An abstract class may or may not have abstract methods. If it has at least one, it cannot be instantiated.
# If no abstract method was defined, then it can be instantiated.
# Use the decorator: @abstractmethod from module abc to set a method as abstract.
# An abstract method may or may not have implementation.
# Python let it very free to change the signature of an abstract method at children of the abstract class.


class Functionary(ABC):
    __slots__ = ["_name", "_cpf", "_address", "_id", "_salary"]

    def __init__(self, name, cpf, address, id_, salary):
        self._name = name
        self._cpf = cpf
        self._address = address
        self._id = id_
        self._salary = salary

    @abstractmethod
    def get_bonus(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_):
        self._id = id_

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def __str__(self):
        return f"{{Name: {self._name}, cpf: {self._cpf}, address: {self._address}, id: {self._id}," \
               f" salary: ${self._salary}}}"


class Administrator(Functionary):

    def __init__(self, name, cpf, address, id_, salary):
        super().__init__(name, cpf, address, id_, salary)

    # Overridden
    def get_bonus(self):
        return self._salary * 0.2


class Director(Functionary):

    def __init__(self, name, cpf, address, id_, salary):
        super().__init__(name, cpf, address, id_, salary)

    def get_bonus(self):
        return self._salary * 0.3


class BonusControl:

    def __init__(self):
        self._total = 0

    def register(self, recordable):  # Duck typing: if it walks like a duck, and quacks like a duck it must be a duck.
        self._total += recordable.get_bonus()

    @property
    def total(self):
        return self._total


if __name__ == "__main__":
    # f1 = Functionary("Rafael Fonseca", "111.222.333-44", Address("Brazil", "GO", "Python land", "High City",
    # "2nd Street Ave. Jh", 12), 1234)
    # If executed, the above line raises a TypeError: abstract classes with abstract methods cannot have direct
    # instances.
    a1 = Administrator("Mark buffalo", "111.222.333-44", Address("U.S.A", "Minnesota", "Cleveland", "center",
                                                                 "Dorian", 1234), 3421, 10000)
    print(a1)
    print(a1.get_bonus())
    # ad = eval(repr(a1.address))
    # print(ad.country)
    d1 = Director("John Mayer", "999.444.111-10", Address("Brazil", "Rio de Janeiro", "Rio de Janeiro", "Leblon",
                                                          "Avenida do País", 982), 8923, 20000)
    bc = BonusControl()
    bc.register(a1)
    print(d1)
    bc.register(d1)
    print(d1.get_bonus())
    print(bc.total)
