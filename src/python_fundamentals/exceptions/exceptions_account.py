class BaseAccountError(Exception):
    pass


class InvalidQuantityError(BaseAccountError):
    def __init__(self, quantity: float):
        super().__init__(f"quantity {quantity} must be >= 0")


class InsufficientFundsError(BaseAccountError):
    def __init__(self, quantity: float):
        super().__init__(f"cannot withdraw quantity {quantity} due tight budget")

