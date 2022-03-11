class Employee:
    def __init__(self, name: str, identification: str, salary: float):
        self._name = name
        self._identification = identification
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @property
    def identification(self):
        return self._identification

    def __str__(self):
        return f"name={self._name}, identification={self._identification}, salary={self._salary}"
