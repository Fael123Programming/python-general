class Point:
    __slots__ = ["_x", "_y"]

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __init(self):
        pass

    # Instances of arbitrary classes can be made callable by defining
    # a __call__() method in their class.
    # The following example __call__() only reassigns new values to
    # both attributes of a point.

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x: float):
        self._x = x

    @y.setter
    def y(self, y: float):
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Point({self._x * 2}, {self._y * 2})"
        # If used eval(repr(point_obj)) will return an object with
        # doubled coordinates comparing with point_obj.

    # Always Python interpreter encounters "+", "-", "*", "/", "%" and pow(base, exponent)
    # it tries to call __add__(), __sub__(), __mult__(), __truediv(), __mod__() and __pow__()
    # from the respective class (magic methods).
    # In this class, it makes sense to override some of them as follows:

    def __add__(self, anotherPoint):
        self.type_check(anotherPoint)
        return Point(self._x + anotherPoint.x, self._y + anotherPoint.y)

    def __sub__(self, anotherPoint):
        self.type_check(anotherPoint)
        return Point(self._x - anotherPoint.x, self._y - anotherPoint.y)

    def __mul__(self, anotherPoint):
        self.type_check(anotherPoint)
        return self._x * anotherPoint.x + self._y * anotherPoint.y  # Actually, scalar product.

    def __truediv__(self, anotherPoint):
        self.type_check(anotherPoint)
        if anotherPoint.x == 0 and anotherPoint.y == 0:
            return Point(0, 0)
        elif anotherPoint.x == 0:
            return Point(0, self._y / anotherPoint.y)
        elif anotherPoint.y == 0:
            return Point(self._x / anotherPoint.x, 0)
        else:
            return Point(self._x / anotherPoint.x, self._y / anotherPoint.y)

    def __mod__(self, anotherPoint):
        self.type_check(anotherPoint)
        if anotherPoint.x == 0 and anotherPoint.y == 0:
            return Point(0, 0)
        elif anotherPoint.x == 0:
            return Point(0, self._y % anotherPoint.y)
        elif anotherPoint.y == 0:
            return Point(self._x % anotherPoint.x, 0)
        else:
            return Point(self._x % anotherPoint.x, self._y % anotherPoint.y)

    def __call__(self, x: float, y: float):
        self._x = x
        self._y = y

    @staticmethod
    def type_check(anObject):
        if not isinstance(anObject, Point):
            raise ValueError("Given argument is not an object from class Point")


if __name__ == "__main__":
    point_obj = Point(1, 5)
    print("First point:", point_obj)
    doubled_point = eval(repr(point_obj))
    print("Another point: x=", doubled_point.x, " y=", doubled_point.y, " then, ", doubled_point)
    print("Sum:", point_obj + doubled_point)
    print("Subtraction:", point_obj - doubled_point)
    print("Scalar product:", point_obj * doubled_point)
    print("Division:", point_obj / doubled_point)
    print("Module:", point_obj % doubled_point)
    print([1, 2, 6] + [19, "Ok", "Java is better than C"] + ["Python is better than Java", 12])
    # Usage of __add__() from class list().
    print(str(True).find("e"))
    print(("T", "u", "e"))
    point_obj(10, 45)  # __call__() is going to be called!
    print(point_obj)

# In Python, numbers, strings and tuples are immutable whereas dictionaries and lists are not.
