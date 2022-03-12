from abc import ABC, abstractmethod
from python_fundamentals.oo.bank_system.main.account_owner import AccountOwner
from python_fundamentals.oo.bank_system.main.exceptions import InsufficientFundsError


class Account(ABC):
    _number_of_accounts = 0

    __slots__ = ["_owner", "_number", "_password", "_agency", "_value_special_check", "_current_balance"]

    def __init__(self, owner: AccountOwner, number: int, password: int, agency: str, value_special_check=0):
        self._owner = owner
        self._number = number
        self._password = password
        self._agency = agency
        self._value_special_check = value_special_check
        self._current_balance = 0
        Account._number_of_accounts += 1

    def withdraw(self, quantity):
        if quantity <= 0:
            raise ValueError("invalid quantity:", quantity)
        if quantity > self._current_balance + self._value_special_check:
            raise InsufficientFundsError()
        self._current_balance -= quantity

    def transfer(self, target, quantity):
        self.withdraw(quantity)
        target.deposit(quantity)

    def deposit(self, quantity):
        if quantity <= 0:
            raise ValueError("invalid quantity:", quantity)
        self._current_balance += quantity

    # Get properties
    @property
    def owner(self):
        return self._owner

    @property
    def number(self):
        return self._number

    @property
    def password(self):
        return self._password

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
        return f"{{owner={self._owner.name}, number={self._number}, agency={self._agency}, value_special_check=${self._value_special_check}, current_balance=${self._current_balance}}}"

    def __eq__(self, another_obj):
        return self._number == another_obj.number and self.get_type() == another_obj.get_type()

    @abstractmethod
    def __repr__(self):
        return f"{self.get_type()}({repr(self._owner)}, {self._number}, \"{self._agency}\")"


class CurrentAccount(Account):

    def __init__(self, owner: AccountOwner, number: int, password: int, agency: str):
        super().__init__(owner, number, password, agency, 0)

    def update(self, tax):
        super().update(tax * 2)

    def __repr__(self):
        return super().__repr__()


class SavingsAccount(Account):

    def __init__(self, owner: AccountOwner, number: int, password: int, agency: str):
        super().__init__(owner, number, password, agency, 0)

    def update(self, tax):
        super().update(tax * 3)

    def __repr__(self):
        return super().__repr__()


class InvestmentAccount(Account):

    def __init__(self, owner: AccountOwner, number: int, password: int, agency: str):
        super().__init__(owner, number, password, agency, 10000)

    def update(self, tax):
        super().update(tax * 5)

    def __repr__(self):
        return super().__repr__()
