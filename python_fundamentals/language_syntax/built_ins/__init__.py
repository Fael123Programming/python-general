#  Built-ins are core resources of Python's standard library such as primitive types and basic functions.
import math
from keyword import kwlist
from string import Formatter
print("Something and something else...")  # This a built-in!
var = type("Something and something else...")  # type() is another built-in!
print(var)  # var is of type str which stands for string (another built-in).
print(type(int("133")))  # Using built-ins one inside another.
complex_number = 23 + 3j  # j represents sqrt(-1) instead of i in mathematics.
print(type(complex_number))
print(complex_number.imag, complex_number.real, str(complex_number.__class__)[8:15:])
# As everything in Python is an object (unlike Java, for example which is not totally object-oriented)
# a variable might have attributes and methods regarding them!
# They belong to pre-definite classes which are also, built-ins.
# Python's standard variable naming uses snake-case:
# Examples: their_car_name, customer_passport_id, next_file.
# Never name a variable with one of the thirty-three keywords of Python.
print("There are", len(kwlist), "keywords in Python. See them written below:")
print("---------------------")
for kw in kwlist:
    print(kw)
print("---------------------")
# format() is a public method and static methods declared in classes Formatter in package string.
# Also, each string object has this method.
enhanced_text_2 = "The number E rounded about of 4 decimal places would be {:.4f}".format(math.e)
print(enhanced_text_2)
print("Do you know how to print {{}} in Python using format()?".format())
print("{2} - {0} - {1} - {0}".format("A", "B", "C"))  # Putting format() arguments in a different order!
print("{:,}".format(2345678))
# The Python equivalent 'null' value is None which refers to an object in memory and occupies space.
