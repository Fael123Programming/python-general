class Employee:
    __slots__ = ["_name", "_cpf", "_salary"]

    def __init__(self, name: str, cpf: str, salary: float):
        self._name = name
        self._cpf = cpf
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf

    @property
    def salary(self):
        return self._salary

    @name.setter
    def name(self, name: str):
        self._name = name

    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf

    @salary.setter
    def salary(self, salary: float):
        self._salary = salary

    def __str__(self):
        return f"Name: {self._name}\tCpf: {self._cpf}\tSalary: ${self._salary}"


class Manager:
    __slots__ = ["_name", "_cpf", "_salary", "_password", "_subordinates"]

    def __init__(self, name: str, cpf: str, salary: float, password: str):
        self._name = name
        self._cpf = cpf
        self._salary = salary
        self._password = password
        self._subordinates = list()

    def authenticate(self, password: str):
        return password == self._password

    def addSubordinate(self, subordinate):
        self._subordinates.append(subordinate)

    def removeSubordinate(self, name: str):
        if len(self._subordinates) == 0:
            return None
        for sub in self._subordinates:
            if sub.name == name:
                subLocal = sub  # Backup variable
                self._subordinates.remove(sub)
                return subLocal
        return None

    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf

    @property
    def salary(self):
        return self._salary

    @property
    def password(self):
        return self._password

    @property
    def subordinates(self) -> list:
        return self._subordinates

    @name.setter
    def name(self, name: str):
        self._name = name

    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf

    @salary.setter
    def salary(self, salary: float):
        self._salary = salary

    @password.setter
    def password(self, password: str):
        self._password = password

    def __str__(self):
        return f"Name: {self._name}\tCpf: {self._cpf}\tSalary: ${self._salary}"
