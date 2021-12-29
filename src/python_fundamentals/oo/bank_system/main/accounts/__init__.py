from abc import ABC, abstractmethod
from python_fundamentals.oo.bank_system.main.account_owner import Owner


class Account(ABC):
    _number_of_accounts = 0

    __slots__ = ["_owner", "_number", "_agency", "_value_special_check", "_current_balance"]

    def __init__(self, owner, number, agency, value_special_check):
        self._owner = owner
        self._number = number
        self._agency = agency
        self._value_special_check = value_special_check
        self._current_balance = 0
        Account._number_of_accounts += 1

    def withdraw(self, quantity):
        if quantity <= 0:
            raise ValueError("invalid quantity")
        if quantity > self._current_balance + self._value_special_check:
            raise ValueError("insufficient funds")
        self._current_balance -= quantity

    def transfer(self, target, quantity):
        self.withdraw(quantity)
        target.deposit(quantity)

    def deposit(self, quantity):
        if quantity <= 0:
            raise ValueError("invalid quantity")
        self._current_balance += quantity

    # Get properties
    @property
    def owner(self):
        return self._owner

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def value_special_check(self):
        return self._value_special_check

    @property
    def current_balance(self):
        return self._current_balance

    # Set properties
    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @number.setter
    def number(self, number):
        self._number = number

    @agency.setter
    def agency(self, agency):
        self._agency = agency

    @value_special_check.setter
    def value_special_check(self, value):
        self._value_special_check = value

    @classmethod
    def number_of_accounts(cls):
        return cls._number_of_accounts

    def get_type(self):
        return self.__class__.__name__

    @abstractmethod
    def update(self, tax):
        self._current_balance += self._current_balance * tax

    def __str__(self):
        return f"Responsible: {self._owner.name}\nAccount number: {self._number}\nAccount type: {self.get_type()}\n" \
               f"Current balance: ${self._current_balance}\nAgency: {self._agency}\n"

    def __eq__(self, another_obj):
        return self._number == another_obj.number and self.get_type() == another_obj.get_type()

    @abstractmethod
    def __repr__(self):
        return f"{self.get_type()}({repr(self._owner)}, {self._number}, \"{self._agency}\")"


class CurrentAccount(Account):

    def __init__(self, owner, number, agency):
        super().__init__(owner, number, agency, 0)

    def update(self, tax):
        super().update(tax * 2)

    def __repr__(self):
        return super().__repr__()


class SavingsAccount(Account):

    def __init__(self, owner, number, agency):
        super().__init__(owner, number, agency, 0)

    def update(self, tax):
        super().update(tax * 3)

    def __repr__(self):
        return super().__repr__()


class InvestmentAccount(Account):

    def __init__(self, owner, number, agency):
        super().__init__(owner, number, agency, 10000)

    def update(self, tax):
        super().update(tax * 5)

    def __repr__(self):
        return super().__repr__()


if __name__ == "__main__":
    c1 = CurrentAccount(Owner("Rafael Fonseca", "St. Avenue 1442 High Hill Los Angeles CA"), 12345, "Cal-1211 GHJ")
    c2 = SavingsAccount(Owner("Mary Kay", "St. Avenue 1456 Genevieve San Francisco CA"), 8923, "SAN-1010 UIS")
    print(c1)
    print(c2)
    print(c1.get_type(), c2.get_type())
    print(repr(c1))
    print(repr(c2))
    c1.deposit(100000)
    c2.deposit(100000)
    c2.transfer(c1, 500)
    c1.update(0.01)
    c2.update(0.02)
    print(c1.current_balance, c2.current_balance)
    c3 = InvestmentAccount(Owner("Natasha Romano", "Wherever"), 1000, "elsewhere")
    print()
    print(c3)
    c3.deposit(9000000)
    c3.update(0.05)
    print(c3.current_balance)
    c3.transfer(c1, 9000000)
    print(c1)
    print(c3)
