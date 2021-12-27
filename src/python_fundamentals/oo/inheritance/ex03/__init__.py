# Testing __repr__() and eval().
# __repr__() is a method inherited from object that acts like __str__
# but is commonly used with eval()
# eval() is a built-in that receives a string and tries to execute it
# as a Python command.
# __str__() is used to show users a more understandable representation of the current object.
# __repr__() is used to give someone else a more technical representation of the object allowing
# someone to get another object from this current object using eval() and repr() inside of it.
# Use repr() to get __repr__() from the object.

class MyClass:
    pass


if __name__ == "__main__":
    an_obj = MyClass()
    print(repr(an_obj))
    print(an_obj.__str__())
    a_command = "print('Let me approximate of you')"
    eval(a_command)
