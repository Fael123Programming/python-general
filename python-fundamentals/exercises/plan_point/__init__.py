class Point:
    number_of_objects = 0  # Static variable! It belongs to the classes.

    def __init__(self, x, y):  # Constructor function.
        self.x, self.y = x, y  # Creating the attributes and assigning them at the same time!
        Point.number_of_objects += 1

    def __str__(self):
        # When a string representation of an object of this classes is required, this method is called out!
        return "({}, {})".format(self.x, self.y)

    # Below we have all own methods of an object of this very classes.

    def sum(self, anotherPoint):
        return Point(self.x + anotherPoint.x, self.y + anotherPoint.y)

    def sub(self, anotherPoint):
        return Point(self.x - anotherPoint.x, self.y - anotherPoint.y)

    def mult(self, anotherPoint):
        return Point(self.x * anotherPoint.x, self.y * anotherPoint * y)

    def div(self, anotherPoint):
        if anotherPoint.x == 0 or anotherPoint.y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Point(self.x / anotherPoint.x, self.y / anotherPoint.y)

    def module(self):
        from math import sqrt
        return sqrt(self.x ** 2 + self.y ** 2)


p1 = Point(1, 3)
p2 = p1.sum(Point(2, 5))
print(p1, "with module", p1.module())
print(p2, "with module", p2.module())
try:
    p1.div(Point(2, 0))
except ZeroDivisionError:
    print("I advised you...")