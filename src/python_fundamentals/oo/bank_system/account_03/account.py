from customer import Customer
from historic import Historic


class Account:
    """
    The class account represents a bank account, its attributes and behaviour. 
    As it handles money mathematical operations are performed inside an 
    object of this class. Also, check of data and related protocols."
    """
    _total_of_accounts = 0  # Class variable
    # We will need a static method or class method to get it accessible either through an object or the class itself:
    # a static method takes no arguments and in the first line above it there comes a decorator @staticmethod;
    # a class method takes one argument which is an object representing the class itself and must have on top
    # of its signature the decorator @classmethod.
    __slots__ = ["_owner", "_number", "_agency", "_limit", "_balance", "_historic", "_ident"]

    # Every class uses a dict to keep the data of each instance (the attribute __dict__).
    # When you define __slots__ and fills it up with the name of some attributes you are
    # avoiding of using __dict__ and dynamic creation of new attributes to an object.
    # Then __slots__ receives a list containing all possible attributes an object of this
    # class may have. Safety purposes!
    # Besides, a class dict spends too much memory space because it has the ability
    # of being dynamically increased (when you add a new couple key/value).
    # __slots__ define a fixed quantity of memory space to be used to an object. 
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
        self._owner = owner  # Object aggregation!!!
        self._number = number
        self._agency = agency
        self._limit = limit
        self._balance = 0.0
        self._historic = Historic()  # Object composition!!!
        Account._total_of_accounts += 1
        self._ident = Account._total_of_accounts
        # Creating the attributes dynamically and initializing them with the values 
        # passed to this constructor function.

    def deposit(self, quantity: float, record=True) -> bool:
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be a floating-point or an integer number")
        if quantity < 0 or self._balance + quantity > self._limit:
            return False  # It did not work...
        self._balance += quantity
        if record:
            self._historic.record_deposit(quantity)
        return True

    def withdraw(self, quantity: float, record=True) -> bool:
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("Argument must be a floating-point or an integer number")
        if quantity < 0 or self._balance < quantity:
            return False  # It did not work...
        self._balance -= quantity
        if record:
            self._historic.record_withdraw(quantity)
        return True

    def transfer_to(self, target, quantity: float) -> bool:
        # 'target' must be another account
        if not isinstance(target, Account):
            raise ValueError("target must be another account")
        if not (isinstance(quantity, float) or isinstance(quantity, int)):
            raise ValueError("quantity must be a floating-point or an integer number")
        if quantity < 0:
            return False
        if self.withdraw(quantity, False):
            if target.deposit(quantity, False):
                self._historic.record_transference(self, target, quantity)
                return True
            self.deposit(quantity, False)
        return False  # Either withdraw() or deposit() did not work.

    # Properties are used to either get object attributes or set new values to them in a more
    # convenient way without having to create strict getters and setters.

    @property
    def owner(self):
        return self._owner

    @property
    def number(self) -> str:
        return self._number

    @property
    def agency(self) -> str:
        return self._agency

    @property
    def limit(self) -> float:
        return self._limit

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def historic(self):
        return self._historic

    @property
    def ident(self):
        return self._ident

    # Setters of some attributes in Python style usign properties.
    # When you try to assign a new value into an object attribute its setter will be called up.

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Customer):
            raise ValueError("owner must be of class Customer")
        self._owner = owner

    @number.setter
    def number(self, number: str):
        self._number = number

    @agency.setter
    def agency(self, agency: str):
        self._agency = agency

    @limit.setter
    def limit(self, limit: float):
        if limit < 1000:
            raise ValueError("limit must be >= 1000")
        self._limit = limit

    @classmethod
    def get_total_of_accounts(cls):
        return cls._total_of_accounts
        # Static methods can be called either by the class itself or an instance of the class.
        # They are not linked to a class of an object but are like common functions outside a
        # class. In inheritance context, static methods cannot be overridden by children of a class.
        # Static methods are immutable.

    @staticmethod
    def class_name():
        return "Account from module account"
        # A class method refers specifically to the class it belongs to.
        # See that it takes as first argument an implicity object which refers to the class.
        # Even though this method can be called by instances like a static method but
        # it can be overridden by children of this class in inheritance context.

    # Magic methods.

    def __str__(self) -> str:
        """
        This method is called when a string 
        representation of an account object is required.
        """
        return f"{{owner: {self._owner}, number: {self._number}, agency: {self._agency}, limit: {self._limit}, balance: {self._balance}}}"

    def __eq__(self, anotherAccount) -> bool:
        """
        This method is used to compare two objects.
        It will be called since a "==" operator is
        being used to compare an account with another object.
        """
        if not isinstance(anotherAccount, Account):
            return False
        return self._number == anotherAccount._number and self._agency == anotherAccount._agency
