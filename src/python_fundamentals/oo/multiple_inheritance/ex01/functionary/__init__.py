class Functionary:
    def __init__(self, name, cpf, address, salary):
        self._name = name
        self._cpf = cpf
        self._address = address
        self._salary = salary

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
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def get_bonus(self, tax):
        return self._salary * tax

