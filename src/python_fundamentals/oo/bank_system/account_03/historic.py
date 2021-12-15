from datetime import datetime
from account import Account


class Historic:
    """
    The class Historic represents objects to be used to keep critical information
    about money transference in an account such as deposits and withdraws.
    Each account must be composed of an object of this class.
    """

    def __init__(self):
        self._opening_date_time = datetime.now()
        self._transactions = list()

    def record_deposit(self, quantity):
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be either a floating-point number or an integer")
        self._transactions.append(f"Deposit of ${quantity} - Date and time: {datetime.now()}")

    def record_withdraw(self, quantity):
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be either a floating-point number or an integer")
        self._transactions.append(f"Withdraw of ${quantity} - Date and time: {datetime.now()}")

    def record_transference(self, origin, target, quantity):
        # origin and target are accounts.
        if not (isinstance(origin, Account) or isinstance(target, Account)):
            raise ValueError("origin and target must be accounts")
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be a floating-point or an integer number")
        self._transactions.append(
            f"Transference of ${quantity} from this account to account {target.number} of agency {target.agency} - Date and time: {datetime.now()}")
        target.historic.transactions.append(
            f"Transference of ${quantity} from account {origin.number} of agency {origin.agency} to this account - Date and time: {datetime.now()}")

    def __str__(self):
        information = "----------------------------------------------------"
        information += f"\nOpening date and time: {self._opening_date_time}"
        if len(self._transactions) == 0:
            information += "\nNo transactions yet"
        else:
            information += "\n--------------------Transactions--------------------"
            for transaction in self._transactions:
                information += "\n" + transaction
        return information

    @property
    def opening_date_time(self) -> datetime:
        return self._opening_date_time

    @property
    def transactions(self) -> list:
        return self._transactions
