class Operation:
    def __str__(self):
        return "An Operation object!"

    @staticmethod
    def shift_right(number, times):
        return number >> times  # Shift bits rightward!

    @staticmethod
    def shift_left(number, times):
        return number << times  # Shift bits leftward!

    @staticmethod
    def multiply(n1, n2):
        return n1 * n2

    @staticmethod
    def divide(n1, n2):
        return n1 / n2  # It may raise a ZeroDivisionError if n2 is 0

    @staticmethod
    def divide_int(n1, n2):
        return n1 // n2  # It may raise a ZeroDivisionError if n2 is 0

    @staticmethod
    def sum(n1, n2):
        return n1 + n2

    @staticmethod
    def sub(n1, n2):
        return n1 - n2

    @staticmethod
    def potentiation(n1, n2):
        return n1 ** n2

    def module(self, n1, n2):
        return n1 % n2

    def concat(self, str1, str2):  # Same as sum()
        return str1 + str2

    def reproduce(self, text, times):  # Same as multiply()
        return text * times

    def isOp(self, object2):
        return self is object2  # 'is' checks whether two variables refer to the same object in memory.
        # Unlike '==', which returns if two contents are equal.

    def inOp(self, value, container):
        return value in container


ops = Operation()
ops2 = ops
print(ops.concat("John ", "Willblock"))
print(ops.concat(1, 2))
print(ops.reproduce("-", 30))
print(ops.reproduce(3, 10))
print(ops)
print(ops.isOp(ops2))
print(ops.isOp(Operation()))  # Comparing with a new-created object.
print(ops is not ops2)
print(ops.inOp(2, [1, 5, 2]))
print(ops.inOp("M", "Marriage?"))
print([1, 2, 3] not in [1, 2, 3, [1, 2, 3]])
print(ops.inOp([1, 2, 3], [1, 2, 3, [1, 2, 3]]))
