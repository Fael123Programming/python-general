import csv


class Item:

    discount_rate = 0.8
    all = dict()

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        self._name = name
        self._price = price
        self._quantity = quantity
        if not Item.all.keys().__contains__(self.__class__.__name__):
            Item.all[self.__class__.__name__] = list()
        Item.all[self.__class__.__name__].append(self)

    def calculate_total_price(self):
        return self._price * self._quantity

    @property  # Read-only attributes!
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        assert 0 < len(name) <= 20, "Name too long!"
        assert name.isalpha(), f"Name {name} must be alphabetic!"
        self._name = name

    @property
    def price(self):
        return self._price

    # Price setters
    def apply_discount(self, percentage: float):
        assert 0 <= percentage <= 1, f"Percentage {percentage} must be between 0 and 1"
        self._price *= percentage

    def apply_increment(self, percentage: float):
        assert 0 <= percentage <= 1, f"Percentage {percentage} must be between 0 and 1"
        self._price *= 1 + percentage

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        assert quantity >= 0, f"Quantity {quantity} must be non-negative"
        self._quantity = quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("/home/leafar/Documents/prg/code/py/python-general/src/python_fundamentals/oo/app/data_persistence"
                  "/items.csv", "r") as file:
            reader = csv.DictReader(file)  # reader contains a collection of dicts caught from items.csv
            list_of_items = list(reader)  # Put all those dicts inside a list.
            for it in list_of_items:
                cls(it.get("name"), float(it.get("price")), int(it.get("quantity")))

    @staticmethod
    def __is_integer(value):  # An example of private method that could be used to perform some business logic here...
        if isinstance(value, int):
            return True
        if isinstance(value, float):
            return value.is_integer()
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
