from datetime import datetime
from accounts import Account
from time import sleep
from exceptions import *


class CashMachine:
    __slots__ = ["_start_datetime", "_agency", "_logged_account"]

    def __init__(self, agency: str):
        self._start_datetime = datetime.today()
        self._agency = agency
        self._logged_account = None

    @property
    def start_datetime(self):
        return self._start_datetime
        
    def log_account(self, account: Account):
        self._check_card_credentials()
        self._check_password(account)
        self._check_fingerprint()
        self._logged_account = account
        print(f"Account of number ({account.number}) owned by ({account.owner.name}) has been logged in")

    def withdraw(self):
        self._check_account_logged_in()
        try:
            self._clean_prompt()
            print("----- Withdraw -----")
            quantity = float(input("Enter the quantity: $"))
            self._clean_prompt()
        except ValueError:
            self._clean_prompt()
            print("Invalid input")
            sleep(1)
        else:
            try:
                self._logged_account.withdraw(quantity) 
            except ValueError as error:
                self._clean_prompt()
                print("invalid quantity: $", quantity)
                sleep(1)
            except InsufficientFundsError as error:
                self._clean_prompt()
                print(error)
                sleep(1)
            else:
                print("Operation done successfully")
                sleep(1)
                self._clean_prompt()

    def deposit(self):
        self._check_account_logged_in()
        try:
            self._clean_prompt()
            print("----- Deposit -----")
            quantity = float(input("Enter the quantity: $"))
            self._clean_prompt()
        except ValueError:
            self._clean_prompt()
            print("Invalid input")
            sleep(1)
        else:
            try:
                self._logged_account.deposit(quantity) 
            except ValueError as error:
                self._clean_prompt()
                print("invalid quantity: $", quantity)
                sleep(1)
            else:
                print("Operation done successfully")
                sleep(1)
                self._clean_prompt()

    def issue_info(self):
        self._check_account_logged_in()
        print("----- Info -----")
        print(self._logged_account)
        input("Hit enter to exit")
        self._clean_prompt()

    def log_out(self):
        self._check_account_logged_in()
        choice = input("Are you sure? [y/n]: ").lower()[0]
        self._clean_prompt()
        while choice not in ["y", "n"]:
            print("Your answer must be either \"y\" or \"n\"...")
            sleep(1)
            self._clean_prompt()
            choice = input("Are you sure? [y/n]: ").lower()[0]
        if choice == "y":
            self._logged_account = None

    def _check_card_credentials(self):
        """Checks whether the card inserted is valid
        and corresponds to an existing account"""
        print("Checking card credentials...")
        sleep(2)
        print("............................ok")
        sleep(1)
        self._clean_prompt()

    def _check_password(self, account: Account):
        """Checks if the given password matches 
        that one record in database"""
        print("Checking password...")
        sleep(2)
        print("....................ok")
        sleep(1)
        self._clean_prompt()

    def _check_fingerprint(self):
        """Asks the customer for their fingerprint
        and evaluates it checking whether is 
        the corresponding fingerprint or not"""
        print("Checking fingerprint...")
        sleep(2)
        print(".......................ok")
        sleep(1)
        self._clean_prompt()

    def _check_account_logged_in(self):
        if self._logged_account is None:
            raise NoneAccountLoggedInError

    @staticmethod
    def _clean_prompt():
        import os
        os.system("cls" if os.name in ("nt", "dos") else "clear")
