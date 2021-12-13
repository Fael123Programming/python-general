from datetime import datetime

class Account:
    """
    The class account represents a bank account, its attributes and behaviour. 
    As it handles money mathematical operations are performed inside an 
    object of this class. Also, check of data and related protocols."
    """
    def __init__(self, owner, number: str, agency: str, limit=1000.0):
        # See that all instance methods have 'self' as first argument.
        # In this method, we perceive that the object was already created by __new__().
        if not isinstance(owner, Customer):
            raise ValueError("owner must be an instance of Customer")
        # All following attributes are of "private" access.
        # To access them, you would have to use: <object>._Account<attribute_name_with_underscores>.
        # When an attribute is defined with '__' Python will automatically rename it as written above.
        # But inside the class, you may mention those "private" attributes as the name you gave them, not
        # the newly created name Python gave them.
        self.__owner = owner  # Object aggregation!!!
        self.__number = number
        self.__agency = agency
        self.__limit = limit
        self.__balance = 0.0
        self.__historic = Historic()  # Object composition!!!
        # Creating the attributes dynamically and initializing them with the values 
        # passed to this constructor function.

    def deposit(self, quantity, record=True):
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be a floating-point or an integer number")
        if quantity < 0 or self.__balance + quantity > self.__limit:
            return False  # It did not work...
        self.__balance += quantity
        if record:
            self.__historic.record_deposit(quantity)
        return True

    def withdraw(self, quantity, record=True):
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("Argument must be a floating-point or an integer number")
        if quantity < 0 or self.__balance < quantity:
            return False  # It did not work...
        self.__balance -= quantity
        if record:
            self.__historic.record_withdraw(quantity)
        return True

    def transfer_to(self, target, quantity):
        # 'target' must be another account
        if not isinstance(target, Account):
            raise ValueError("target must be another account")
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be a floating-point or an integer number")    
        if quantity < 0:
            return False
        if self.withdraw(quantity, False):
            if target.deposit(quantity, False):
                self.__historic.record_transference(self, target, quantity)
                return True
            self.deposit(quantity, False)    
        return False  # Either withdraw() or deposit() did not work.

    def __str__(self):
        """
        This method is called when a string 
        representation of an account object is required.
        """
        return f"{{owner: {self.__owner}, number: {self.__number}, agency: {self.__agency}, limit: {self.__limit}, balance: {self.__balance}}}"

    def __eq__(self, anotherAccount):
        """
        This method is used to compare two objects.
        It will be called since a "==" operator is
        being used to compare an account with another object.
        """
        if not isinstance(anotherAccount, Account):
            return False
        return self.__number == anotherAccount.__number and self.__agency == anotherAccount.__agency


class Customer:
    """
    The class Customer represents a simple customer data set that contains basic informations
    about a customer which would be significant in a prototype of a bank system.
    """
    def __init__(self, name: str, dateOfBirth: str, cpf: str):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__cpf = cpf

    def __str__(self):
        return f"{{name: {self.__name}, dateOfBirth: {self.__dateOfBirth}, cpf: {self.__cpf}}}"


class Historic:
    """
    The class Historic represents objects to be used to keep critical information
    about money transferences in an account such as deposits and withdraws.
    Each account must be composed of an object of this class.
    """
    def __init__(self):
        self.__opening_date_time = datetime.now()
        self.__transactions = list()

    def record_deposit(self, quantity):
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be either a floating-point number or an integer")
        self.__transactions.append(f"Deposit of ${quantity} - Date and time: {datetime.now()}")

    def record_withdraw(self, quantity):
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be either a floating-point number or an integer")
        self.__transactions.append(f"Withdraw of ${quantity} - Date and time: {datetime.now()}")

    def record_transference(self, origin, target, quantity):
        # origin and target are accounts.
        if not (isinstance(origin, Account) or isinstance(target, Account)):
            raise ValueError("origin and target must be accounts")
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be a floating-point or an integer number")
        self.__transactions.append(f"Transference of ${quantity} from this account to account {target._Account__number} of agency {target._Account__agency} - Date and time: {datetime.now()}")
        target._Account__historic._Historic__transactions.append(f"Transference of ${quantity} from account {origin._Account__number} of agency {origin._Account__agency} to this account - Date and time: {datetime.now()}")

    def __str__(self):
        information = "----------------------------------------------------"
        information += f"\nOpening date and time: {self.__opening_date_time}"
        if len(self.__transactions) == 0:
            information += "\nNo transactions yet"
        else:
            information += "\n--------------------Transactions--------------------"
            for transaction in self.__transactions:
                information += "\n" + transaction
        return information