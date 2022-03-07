from src.python_fundamentals.oo.app.classes.item import Item


class Phone(Item):

    discount_rate = 0.7  # Changing the value of a variable inherited from a super class

    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        super().__init__(name, price, quantity)
        self.__broken_phones = broken_phones

    @property
    def broken_phones(self):
        return self.__broken_phones

    @broken_phones.setter
    def broken_phones(self, value: int):
        assert value >= 0, f"Broken phones {value} must be non-negative"
        assert value <= self.quantity, "Invalid quantity of broken phones"
        self.__broken_phones = value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"
