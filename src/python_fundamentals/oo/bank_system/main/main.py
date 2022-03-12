from accounts import CurrentAccount
from account_owner import AccountOwner
from address import Address
from datetime import date
from cash_machine import CashMachine


if __name__ == "__main__":
    my_address = Address(
        "Brazil", "RJ",
        "Rio de Janeiro",
        "Santo Gaio",
        "Alfredo Neves",
        212,
        "Of course this is a fake address :)"
    )
    me = AccountOwner(
        "Rafael Fonseca",
        my_address,
        "Almost a programmer",
        date(
            2002,
            6,
            11
        )
    )
    my_account = CurrentAccount(
        me,
        12345,
        54321,
        "RJ Agency"
    )
    cash_machine = CashMachine(
        "RJ Agency"
    )
    cash_machine.log_account(
        my_account
    )
    cash_machine.deposit()
    cash_machine.withdraw()
    cash_machine.issue_info()
    cash_machine.deposit()
    cash_machine.issue_info()
    cash_machine.log_out()
    print(
        cash_machine.start_datetime
    )
