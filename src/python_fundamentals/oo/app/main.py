from src.python_fundamentals.oo.app.classes.item import Item
from src.python_fundamentals.oo.app.classes.phone import Phone

# OOP main principles: encapsulation, abstraction, inheritance and polymorphism

if __name__ == "__main__":
    Item.instantiate_from_csv()
    p1 = Phone("Samsung Galaxy 10", 250, 30)
    print(Item.all["Phone"])
    print(p1.broken_phones)
    print("""
    Hello Python...
    """)
