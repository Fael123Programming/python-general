import csv
# cvs stands for "comma separated values" which is a type of data organization and also, a file type.


class Item:

    discount_rate = 0.8
    all = list()

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.discount_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("/home/leafar/Documents/prg/code/py/python-general/src/python_fundamentals/oo/app/data_persistence"
                  "/items.csv", "r") as file:
            reader = csv.DictReader(file)  # reader contains a collection of dicts caught from items.csv
            list_of_items = list(reader)  # Put all those dicts inside a list.
            for it in list_of_items:
                cls(it.get("name"), float(it.get("price")), int(it.get("quantity")))

    @staticmethod
    def is_integer(value):
        if isinstance(value, int):
            return True
        if isinstance(value, float):
            return value.is_integer()
        return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    all = list()

    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones
        Phone.all.append(self)

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"


if __name__ == "__main__":
    Item.instantiate_from_csv()
    p1 = Phone("Samsung A90", 500, 10)
    p2 = Phone("Iphone X+", 1000, 5)
    print(Item.all)
    print(Phone.all)
