from python_fundamentals.exceptions.exceptions_account import InvalidQuantityError, InsufficientFundsError


class Account:
    def __init__(self, owner_name: str, number: int, limit=0):
        self._owner_name = owner_name
        self._number = number
        self._balance = 0
        self._limit = limit

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def number(self):
        return self._number

    @property
    def balance(self):
        return self._balance

    @property
    def limit(self):
        return self._limit

    def deposit(self, quantity: float):
        if quantity < 0:
            raise InvalidQuantityError(quantity)
        self._balance += quantity

    def withdraw(self, quantity: float):
        if quantity < 0:
            raise InvalidQuantityError(quantity)
        if quantity > self._balance + self._limit:
            raise InsufficientFundsError(quantity)
        self._balance -= quantity

    def __str__(self):
        return f"owner_name={self._owner_name}, number={self._number}"


if __name__ == "__main__":
    c1 = Account("Jones", 5001)
    print(c1)
    c1.deposit(100)
    c1.withdraw(200)
