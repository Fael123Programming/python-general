from python_fundamentals.oo.bank_system.main.account_owner import AccountOwner
from python_fundamentals.oo.bank_system.main.account_repository.account_collections import AccountsMapping
from python_fundamentals.oo.bank_system.main.accounts import CurrentAccount, Account, SavingsAccount


def cast_to_account(account_data: list, account_type: str) -> Account:
    from python_fundamentals.oo.bank_system.main.address import Address
    from datetime import date

    account_type = account_type.strip().lower()
    if account_type == "current account":
        new_account = CurrentAccount(
            AccountOwner(
                account_data[0],
                Address(
                    account_data[1],
                    account_data[2],
                    account_data[3],
                    account_data[4],
                    account_data[5],
                    int(account_data[6])
                ),
                account_data[7],
                date(
                    int(account_data[8]),
                    int(account_data[9]),
                    int(account_data[10])
                )
            ),
            int(account_data[11]),
            int(account_data[12]),
            account_data[13]
        )
    elif account_type == "savings account":
        new_account = SavingsAccount(
            AccountOwner(
                account_data[0],
                Address(
                    account_data[1],
                    account_data[2],
                    account_data[3],
                    account_data[4],
                    account_data[5],
                    int(account_data[6])
                ),
                account_data[7],
                date(
                    int(account_data[8]),
                    int(account_data[9]),
                    int(account_data[10])
                )
            ),
            int(account_data[11]),
            int(account_data[12]),
            account_data[13]
        )
    else:
        raise TypeError("Unknown account type:", account_type)
    new_account.deposit(float(account_data[14]))
    return new_account


if __name__ == "__main__":

    from python_fundamentals.oo.bank_system.main.address import Address
    from datetime import date
    import csv

    with open("account_repo.csv") as current_accounts_file:
        csv_reader = csv.reader(current_accounts_file)
        accounts = AccountsMapping()
        for element in csv_reader:
            account_created = cast_to_account(element, "current account")
            accounts[account_created.number] = account_created
    for key, value in accounts.items():
        print(accounts[key].owner.name, accounts[key].current_balance, accounts[key].__class__.__name__, sep=" ")

