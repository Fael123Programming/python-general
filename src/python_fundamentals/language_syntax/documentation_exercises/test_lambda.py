def make_incrementor(n):
    return lambda x: x + n  # This function returns another function.


def operate(function, arg1: float | int, arg2: float | int) -> float:
    return function(arg1, arg2)  # This function returns the result of another function applied on two arguments.


class Calculator:
    """This is a simple a calculator that calculates operations over two arguments in a single method.

        A use of this class would lead to creation of lambda expressions and a large use of them.
    """
    def __init__(self, operation):
        self._operation = operation

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, operation):
        self._operation = operation

    def calculate(self, value_a: float | int, value_b: float | int):
        return self._operation(value_a, value_b)


def f(ham: str, eggs: str = 'eggs') -> str:  # This header contains three function annotations.
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


if __name__ == "__main__":
    plus_one = make_incrementor(1)
    var = 5
    print(plus_one(var))
    print(operate(lambda a, b: a+b, 100, 200))  # Passing a function as argument!
    print(operate(lambda a, b: a-b, 200, 100))
    print("----------------------------------")
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)
    calc = Calculator(lambda a, b: a + b)
    print(calc.calculate(100, 100))
    calc.operation = lambda a, b: a / b if b != 0 else None
    print(calc.calculate(100, 2), calc.calculate(90, 0))
    print(Calculator.__doc__)
    my_string = "Python"
    print(my_string.encode())
