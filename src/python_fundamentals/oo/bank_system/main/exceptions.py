class BaseAccountError(RuntimeError):
    pass


class InsufficientFundsError(BaseAccountError):
    def __init__(self):
        super().__init__("You do not have enough money")


class NoneAccountLoggedInError(BaseAccountError):
    def __init__(self):
        super().__init__("None account was found logged in")
