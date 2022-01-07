import random
from abc import ABC, abstractmethod


class Taxable(ABC):  # Class that will have virtual subclasses...
    # No multiple inheritance will need to be applied with this feature!
    # It just needed to use the register() method from ABC

    @abstractmethod
    def get_tax(self):
        pass


class Transport(ABC):

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):

    # Its code comes here!

    def deliver(self):
        print("Delivering delivery through a truck...")

    def get_tax(self):
        return random.randint(1, 1000) * random.random()


class Ship(Transport):

    # Its code comes here...

    def deliver(self):
        print("Delivering delivery through a ship...")

    def get_tax(self):
        return random.randint(1, 10000) * random.random()


if __name__ == "__main__":
    Taxable.register(Truck)
    Taxable.register(Ship)
    t1 = Truck()
    s1 = Ship()
    if isinstance(t1, Taxable):
        print("A truck is taxable")
    if isinstance(s1, Taxable):
        print("A ship is taxable")
    # By this mean, it is better to use isinstance() and issubclass() instead of the simple hasattr()!
