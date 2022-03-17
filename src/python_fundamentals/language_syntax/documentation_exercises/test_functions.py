def fib(n: int):
    assert n > 0, f"{n} must be greater than zero"
    a, b = 0, 1
    values = list()
    while a < n:
        values.append(a)
        a, b = b, a + b
    return values


class Person:
    __slots__ = ["_name"]

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


def change(var):  # var does not get changed permanently. Arguments are passed by value.
    var = 100


def change_name(person: Person):
    person.name = input("Enter new name: ")


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes', 'yep'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries == 0:
            raise ValueError('invalid user response')
        print(reminder)


if __name__ == "__main__":
    # fib(30)
    # var = "Rafael"
    # change(var)
    # print(var)
    # eric = Person("Eric")
    # print(eric.name)
    # eric.name = "Mariano"
    # print(eric.name)
    # print(fib)
    # calc_fibonacci = fib
    # print(calc_fibonacci)
    # print(calc_fibonacci(900))
    # print(fib(900))
    # me = Person("Rafael")
    # change_name(me)
    # print("Name got updated: " + me.name)
    if ask_ok("Do you really want to quit? [y/n]: "):
        print("Bye bye")
    else:
        print("Let us move on")
