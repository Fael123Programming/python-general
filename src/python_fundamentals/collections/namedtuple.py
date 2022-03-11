from collections import namedtuple

if __name__ == "__main__":
    Car = namedtuple("Car", "brand, model, color, price")  # Creating the type.
    my_car = Car("Ford", "F-150 Raptor", "Black", 100000)  # Instantiating the type.
    print(my_car)
    print(f"My {my_car.model} is worth ${my_car.price}")  # Accessing instance attributes through dot operator.
    print(f"My {my_car[1]} is worth ${my_car[3]}")  # Accessing instance attributes through index.
    try:
        my_car.price = 1000  # Is possible to set it cheaper?
    except AttributeError:
        print("No! It is not possible because named tuples are immutable")


