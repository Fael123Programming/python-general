from python_fundamentals.oo.inheritance.ex02.address import Address


class Person:
    __slots__ = ["_name", "_address"]

    def __init__(self, name: str, address: Address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @name.setter
    def name(self, name: str):
        self._name = name

    @address.setter
    def address(self, address):
        self._address = address


class User(Person):
    __slots__ = ["_password"]

    def __init__(self, name: str, address: Address, password: int):
        super().__init__(name, address)
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: int):
        self._password = password


class PhysicalPerson(User):
    __slots__ = ["_cpf"]

    def __init__(self, name: str, address: Address, password: int, cpf: str):
        super().__init__(name, address, password)
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf


class LegalPerson(User):
    __slots__ = ["_cnpj"]

    def __init__(self, name: str, address: Address, password: int, cnpj: str):
        super().__init__(name, address, password)
        self._cnpj = cnpj

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        self._cnpj = cnpj
