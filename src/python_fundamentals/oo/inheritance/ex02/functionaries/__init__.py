from python_fundamentals.oo.inheritance.ex02.person_hierarchy import PhysicalPerson
from python_fundamentals.oo.inheritance.ex02.address import Address


class Employee(PhysicalPerson):
    __slots__ = ["_salary", "_id"]

    def __init__(self, name: str, address: Address, password: int, cpf: str, salary: float, id_: int):
        super().__init__(name, address, password, cpf)
        self._salary = salary
        self._id = id_

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary: float):
        self._salary = salary

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id: int):
        self._id = new_id

    def get_bonus(self):
        return self._salary * 0.1  # 10% of the salary at the end of the year is given to each employee.

    def __str__(self):  # Overridden method from class object: the mom of every class in Python.
        return f"Name: {self._name} \t Cpf: {self._cpf} \t Salary: ${self._salary} \t Id: {self._id}"


class Manager(Employee):
    __slots__ = ["_subordinates"]

    def __init__(self, name: str, address: Address, password: int, cpf: str, salary: float, id_: int):
        super().__init__(name, address, password, cpf, salary, id_)
        # The method super() makes that you reference to the super class of this class.
        # Using it you may call methods from it.
        # In this case, we're calling the proper constructor function.
        self._subordinates = list()

    @property
    def subordinates(self):
        return self._subordinates

    def addSubordinate(self, subordinate):
        self._subordinates.append(subordinate)

    def removeSubordinate(self, id_: int):
        if len(self._subordinates) == 0:
            return None
        for sub in self._subordinates:
            if sub.id == id_:
                subLocal = sub
                self._subordinates.remove(sub)
                return subLocal
        return None

    def get_bonus(self):  # Overridden method from super class.
        return self._salary * 0.15  # 15% of the salary of each manager is given to them at the end of the year.
