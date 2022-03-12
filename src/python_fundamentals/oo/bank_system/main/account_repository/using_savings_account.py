from python_fundamentals.oo.bank_system.main.account_repository.account_collections import Accounts
from using_current_accounts import cast_to_account


if __name__ == "__main__":
    import csv

    with open("account_repo.csv") as account_repo:
        csv_reader = csv.reader(account_repo)
        accounts = Accounts()
        for element in csv_reader:
            accounts.append(cast_to_account(element, "savings account"))
        for account in accounts:
            print(account.owner.name, account.current_balance, account.__class__.__name__, sep=" ")


