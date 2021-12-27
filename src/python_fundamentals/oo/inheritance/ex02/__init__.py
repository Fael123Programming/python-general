from python_fundamentals.oo.inheritance.ex02.functionaries import *
from python_fundamentals.oo.inheritance.ex02.control_of_bonuses import ControlOfBonuses


if __name__ == "__main__":
    emp1 = Employee("Rafael Fonseca", Address(), 12345, "111.222.333-44", 10000, 78322)
    emp2 = Manager("Marianna Neves", Address(), 54321, "777.888.333-11", 15000, 82123)
    print("emp1:", emp1)
    print("emp2:", emp2)
    emp2.addSubordinate(emp1)
    print("emp2 first subordinate:", emp2.subordinates[0])
    emp2.addSubordinate(Manager("Paulo Fonseca", Address(), 98765, "999.111.333-73", 5000, 91123))
    print("emp2 all subordinates:", emp2.subordinates)
    print("emp2 second subordinate:", emp2.subordinates[1])
    emp2.removeSubordinate(78322)
    print(emp2.subordinates)
    print(emp2.get_bonus(), emp1.get_bonus())
    print(emp2.__slots__)
    print(emp1.__slots__)
    print(emp2.name)
    control = ControlOfBonuses()
    control.register(emp1)
    control.register(emp2)
    control.register(emp2.subordinates[0])
    control.register(ControlOfBonuses())
    print("Total:", control.total)
