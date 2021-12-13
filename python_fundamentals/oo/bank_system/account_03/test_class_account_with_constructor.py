from account import *
# Important things in Python:
# -> You do not have to use the 'new' operator to create an object;
# -> Inside a class, there must be used 'self' instead of the popular 'this' to refer to objects;
# -> See that all instance methods have 'self' as first parameter;
# -> Like Java and another languages, you never have an object itself on the code but a reference
# variable (that points to a memory address) to an object on your code;
# -> Using the '==' operator with objects will compare the memory addresses where they are;
# -> In Python we have only passing of arguments to any function by reference, that is, we do not
# have argument copies being made.

acc1 = Account(Customer("Jorge Simons", "12-03-1990", "123456-45"), "123-45", "Tya-12", 2000)
print(acc1._Account__balance)  # Terrible practice! It should never be done: access a "private" attribute directly.
print(acc1._Account__agency)
acc1.deposit(100)
acc1.deposit(1900)
print(acc1)
acc1.withdraw(20000)  # Failed...
acc1.withdraw(2000)
print(acc1)
acc2 = acc1  # acc2 will point to the same memory address acc1 already points to.
acc2.deposit(5)
print(acc1)
# The builtin id() returns the memory reference of an object.
print(id(acc1), id(acc2), "Are they equal?", id(acc1) == id(acc2))
acc3 = Account(Customer("Jorge Simons", "12-03-1990", "123456-45"), "123-45", "Tya-12", 2000)
acc3.deposit(5)
print(acc1)
print(acc3)
print(acc1 == acc3)  # Method __eq__ was overriden.
print(acc1 == acc2)
print(acc2 == acc3)
acc3.transfer_to(acc1, 5)
print(acc1)
print(acc3)
print(acc3._Account__owner._Customer__name)
print(type(acc3._Account__owner))
print(type(acc3._Account__balance))  # Everything in Python is an object!
print(acc3._Account__historic)
print()
print(acc1._Account__historic)

# Some special attributes and methods are by standard added to every class by interpreter.
print(dir(Account))  # dir() gives a string containing all those things from an object or class!!!
print(acc1.__class__)
print(acc1.__dict__)  # All attributes of an object.
print(vars(acc1))  # The same of calling acc1.__dict__
print(acc1.__doc__)  # __doc__ gives the information put within """ """.
print(acc1._Account__historic.__doc__)
print(acc1._Account__owner.__doc__)
print(acc1.__eq__.__doc__)
print(acc1.__module__)

# All methods surrounded by double underscores are called as magic methods.
# Actually, a class uses a dictionary to hold its definite attributes. See vars() and __dict__.
# In Python we do not have access modifiers (or visibility modifiers) but underscores that are
# used to only imply that some attributes should never be accessed directly.
# Put __ before the name of the newly created attribute to define it as "private".
# If we do mention to the attributes of the classes we are handling (remember that they are private) 
# as the name we have them inside the class (__ put before the name), Python will actually create 
# dynamically new attributes. There goes an example:
print(dir(acc1))
acc1.__agency = "new attribute created at runtime dynamically. It is not _Account__agency"
print(dir(acc1))
# So there will exist concomitantly _Account__agency (defined as "private" inside constructor) 
# and __agency (which is not "private").
print(acc1.__agency)
print(acc1._Account__agency)
# We have looked at how privacity of attributes are made. But how do I define an attribute as protected?
# Indeed, we do not have this concept in the core of Python but programmers have created a standard to 
# create this type of attributes: you just have to write a single underscore before the name of the specific
# attribute when creating it inside constructor. Nothing further will be made by interpreter. It is just a 
# convention. It means that that attribute should never be accessed directly. Python community does not like to 
# use private conceptv very well.
president_account = Account(Customer("Jair Messias Bolsonaro", "10-15-1969", "123123123123-123123"), "312312/23", "Brazilia", limit=100000)
print(president_account._Account__historic)