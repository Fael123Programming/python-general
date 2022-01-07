from src.python_fundamentals.oo.multiple_inheritance.ex01.internal_system import InternalSystem
from src.python_fundamentals.oo.multiple_inheritance.ex01.director import Director
from src.python_fundamentals.oo.multiple_inheritance.ex01.manager import Manager
from src.python_fundamentals.oo.multiple_inheritance.ex01.functionary import Functionary


if __name__ == "__main__":
    system = InternalSystem()
    d1 = Director("Jozé", "123435", "Rio de Janeiro 345", 10000, "finance")
    m1 = Manager("Mateus", "0123092", "Rio de Janeiro 567", 5000)
    f1 = Functionary("Pamela", "431922", "São Paulo 122", 8000)
    try:
        system.login(d1)
        system.login(m1)
        system.login(f1)
    except AttributeError as ae:
        print("Some functionaries are not authenticable:", ae)