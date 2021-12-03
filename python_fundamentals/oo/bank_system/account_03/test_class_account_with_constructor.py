from account import Account

# Important things in Python:
# -> You do not have to use the 'new' operator to create an object
# -> Inside a class, there must be used 'self' instead of the popular 'this' to refer to objects.
# -> See that all instance methods have 'self' as first parameter.
# -> Like Java and another languages, you never have an object itself on the code but a reference
# variable (that points to a memory address) to an object on your code.
# -> Using the '==' operator with objects will compare the memory addresses where they are.
# -> In Python we have only passing of arguments to any function by reference, that is, we do not
# have argument copies being made.
acc1 = Account("Jorge Simons", "123-45", "Tya-12", 2000)
print(acc1.balance) 
print(acc1.agency)
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
acc3 = Account("Jorge Simons", "123-45", "Tya-12", 2000)
acc3.deposit(5)
print(acc1)
print(acc3)
print(acc1 == acc3)
print(acc1 == acc2)
print(acc2 == acc3)
acc3.transfer_to(acc1, 5)
print(acc1)
print(acc3)