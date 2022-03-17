def http_error(error_code: int) -> str:
    match error_code:
        case 404:
            return "not found"
        case 400:
            return "bad request"
        case _:  # This is the equivalent to the default branch!
            return "unknown error code"


def is_a_number(obj: object):
    match obj.__class__.__name__:
        case "int" | "float":  # '|' means or.
            return True
        case _:
            return False


def depict_point(point: tuple):
    match point:
        case (0, 0):  # Comparing it against two literals!
            return "origin"
        case (0, y):
            return f"y={y}"
        case (x, 0):
            return f"x={x}"
        case (x, y):
            # Comparing it against two bound variables (they were assigned with the values that 'point' holds)!
            return f"x={x}, y={y}"
        case _:
            raise ValueError("Not a point")


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


def where_is(point: Point):
    match point:
        case Point(x=0, y=0):
            return "origin"
        case Point(x=0, y=y):
            return f"y={y}"
        case Point(x=x, y=0):
            return f"x={x}"
        case Point(x=x, y=y):
            return f"x={x}, y={y}"
        case _:
            return "not a point"


def match_points(roster_of_points: list):
    match roster_of_points:
        case []:
            return "empty roster"
        case [Point(x=0, y=0)]:
            return "the origin"
        case [Point(x=x, y=y)]:
            return f"single point: x={x}, y={y}"
        case [Point(x=0, y=y1), Point(x=0, y=y2)]:
            return f"two points on the Y axis at {y1}, {y2}"
        case [Point(x=x1, y=0), Point(x=x2, y=0)]:
            return f"two points on the X axis at {x1}, {x2}"
        case _:
            return "something else"


def match_with_if(point: Point):
    match point:
        case Point(x=x, y=y) if x == y:
            return f"y=x at {x}"
        case _:
            return "default"


def match_logic(value):
    #  True, False and None are unique objects from their classes!
    #  They are compared by their identities.
    match value:
        case True:
            return "true"
        case False:
            return "false"
        case None:
            return "none"


if __name__ == "__main__":
    print(http_error(404))
    print(is_a_number("bla bla"))
    print(is_a_number(100))
    print(is_a_number(3.567))
    print(is_a_number(False))
    print(depict_point((1, 15)))
    print(depict_point((0, 100)))
    print(depict_point((78, 0)))
    try:
        print(depict_point("point"))
    except ValueError:
        print("A value error has been thrown")
    print(where_is("point"))
    var = 100
    print(where_is(Point(x=var, y=80)))
    print(match_points([Point(0, 9), Point(0, 11)]))
    print(match_points([Point(0, 0)]))
    print(match_points([Point(10, 50)]))
    print(match_points([Point(12, 0), Point(51, 0)]))
    print(match_points([Point(150, 510)]))
    print(match_with_if(Point(1, 1)))
    print(match_logic(False))
    print(match_logic(True))
    print(match_logic(None))
