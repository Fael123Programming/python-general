# In Python, we do not care about which class an object belongs to intrinsically
# but only if it knows or not to do something, that is, if it has or not a specific
# attribute.
# Duck typing is a concept related to dynamic typing, where the type or the class of
# an object is less important than the methods it defines. When you use duck typing,
# you do not check types at all. Instead, you check for the presence of a given method
# or attribute.
# Basically, it says "if it walks like a duck, and it quacks like a duck, then it must be a duck".

class Duck:

    def quack(self):
        print(f"Quack quack from object at {id(self)}!")


class Goose:

    def quack(self):
        print(f"Quack quack from object at {id(self)}!")


class Car:
    pass


class Validator:

    @staticmethod
    def check_it_quacks(possible_duck):
        try:
            possible_duck.quack()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    checker = Validator()
    checker.check_it_quacks(Duck())
    checker.check_it_quacks(Goose())
    checker.check_it_quacks(Car())
