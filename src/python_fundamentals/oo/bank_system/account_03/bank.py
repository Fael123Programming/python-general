from python_fundamentals.oo.bank_system.account_03.account import *
from python_fundamentals.oo.bank_system.account_03.account_updater import AccountUpdater


class Bank:
    __slots__ = ["_accounts"]

    def __init__(self):
        self._accounts = list()

    @property
    def accounts(self):
        return self._accounts

    def add_account(self, acc):
        self._accounts.append(acc)

    def del_account(self, id_):
        for acc in self._accounts:
            if hasattr(acc, "_ident") and id_ == acc.ident:
                self._accounts.remove(acc)
                return True
        return False  # Account not found

    def get_account(self, id_):
        if len(self._accounts) == 0:
            raise ValueError("None accounts were created so far")
        for acc in self._accounts:
            if hasattr(acc, "_ident") and acc.ident == id_:
                return acc

    def total_of_accounts(self):
        return len(self._accounts)


if __name__ == "__main__":
    bk = Bank()
    bk.add_account(CurrentAccount("Macon Jones", "1231", "agency one"))
    bk.add_account(SavingsAccount("Chris Evans", "9123", "agency one"))
    bk.add_account(Account("Marinna Silva", "10101", "agency three"))
    print(bk.total_of_accounts())
    bk.get_account(1).deposit(500)
    bk.get_account(2).deposit(500)
    bk.get_account(3).deposit(500)
    updater = AccountUpdater(0.013)
    for account in bk.accounts:
        updater.calculate(account)
    bk.del_account(2)
    print(bk.total_of_accounts())
    print(bk.get_account(1))
    print(bk.get_account(3))
