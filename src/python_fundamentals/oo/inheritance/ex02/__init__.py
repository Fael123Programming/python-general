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

    def __str__(self):
        return f"Name: {self._name}\tCpf: {self._cpf}\tSalary: ${self._salary}"


class Manager(Employee):
    __slots__ = ["_password", "_subordinates"]

    def __init__(self, name: str, cpf: str, salary: float, password: str):
        super().__init__(name, cpf, salary)
        self._password = password
        self._subordinates = list()


