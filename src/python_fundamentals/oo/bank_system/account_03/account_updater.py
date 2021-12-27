from python_fundamentals.oo.bank_system.account_03.account import *


class AccountUpdater:
    __slots__ = ["_selic", "_total_of_balances"]

    def __init__(self, selic_tax: float):
        self._selic = selic_tax
        self._total_of_balances = 0.0

    @property
    def selic(self):
        return self._selic

    @selic.setter
    def selic(self, selic: float):
        self._selic = selic

    @property
    def total_of_balances(self):
        return self._total_of_balances

    def calculate(self, account):
        print("Former balance: ${}".format(account.balance))
        self._total_of_balances += account.update(self._selic)
        print("Updated balance: ${}".format(account.balance))


class AnotherThing:
    def __init__(self, value):
        self._value = value

    def update(self, value):
        return self._value + value

    @property
    def balance(self):
        return self._value


if __name__ == "__main__":
    acc1 = Account("Rafael Fonseca", "1234", "agency 1")
    acc2 = CurrentAccount("John Wesley", "56789", "agency 1")
    acc3 = SavingsAccount("Andrea Menezes", "908123", "agency 2")
    acc1.deposit(500)
    acc2.deposit(800)
    acc3.deposit(300)
    updater = AccountUpdater(0.01)
    updater.calculate(acc1)
    updater.calculate(acc2)
    updater.calculate(acc3)
    updater.calculate(AnotherThing(200))  # AnotherThing is not an account but signs the contract!
    # This is quite a clear example of duck typing in Python.
    # Not matter the class of an object but what it has as attributes!
    print(acc1)
    print(acc2)
    print(acc3)

