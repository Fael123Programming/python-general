class Account:
    # Here somewhere comes the function __new__() that creates the object. 
    def __init__(self, owner_name: str, number: str, agency: str, limit: float):
        # See that all instance methods have 'self' as first argument.
        # In this method, we perceive that the object was already created by __new__().
        self.owner_name = owner_name
        self.number = number
        self.agency = agency
        self.limit = limit
        self.balance = 0.0
        # Creating the attributes dynamically and initializing them with the values 
        # passed to this constructor function.

    def deposit(self, quantity: float):
        if quantity < 0 or self.balance + quantity > self.limit:
            return False  # It did not work...
        self.balance += quantity
        return True

    def withdraw(self, quantity: float):
        if quantity < 0 or self.balance < quantity:
            return False  # It did not work...
        self.balance -= quantity
        return True

    def transfer_to(self, target, quantity: float):
        if quantity < 0:
            return False
        if self.withdraw(quantity):
            if target.deposit(quantity):
                return True
            self.deposit(quantity)    
        return False  # Either withdraw() or deposit() did not work.

    def __str__(self):
        # This method is like toString() from Java: it is called when a string representation of an4 object is required.
        return f"{{owner_name: {self.owner_name}, number: {self.number}, agency: {self.agency}, limit: {self.limit}, balance: {self.balance}}}"
