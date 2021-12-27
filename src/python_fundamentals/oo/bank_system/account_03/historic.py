from datetime import datetime


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
        self._transactions.append(f"Deposit of ${quantity} - Date and time: {datetime.now()}")

    def record_withdraw(self, quantity):
        self._transactions.append(f"Withdraw of ${quantity} - Date and time: {datetime.now()}")

    def record_transference(self, origin, target, quantity):
        self._transactions.append(
            f"Transference of ${quantity} from this account to account {target.number} of agency {target.agency} - "
            f"Date and time: {datetime.now()}")
        target.historic.transactions.append(
            f"Transference of ${quantity} from account {origin.number} of agency {origin.agency} to this account - "
            f"Date and time: {datetime.now()}")

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
