import abc  # Abstract Base Class module.
# All abstract classes in Python inherit from abc.ABC.


class BasePizza(abc.ABC):

    @abc.abstractmethod
    def get_radius(self):
        pass

    # Doing this way BasePizza cannot be instantiated
    # directly. All its children will have to give an
    # implementation to get_radius().
    # Trying BasePizza() will raise a TypeError.
    # You can change the prototype of an abstract method
    # when implementing it like set another parameter list, 
    # put new decorators etc.
    # Differently of Java and another programming languages
    # abstract methods in Python can have implementations.


class Pizza(BasePizza):

    @staticmethod
    def get_radius(param1):
        return "get_radius() from Pizza instance " + str(param1)


class FakePizza(BasePizza):
    pass


if __name__ == "__main__":
    print(Pizza().get_radius)  # Bound method on an object.
    print(Pizza().get_radius(1))
    # print(FakePizza())  # Cannot instantiate this class because it did not implement get_radius().
