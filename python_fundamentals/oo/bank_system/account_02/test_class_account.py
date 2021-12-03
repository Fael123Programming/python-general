from account import Account

my_account = Account()
# Python differs a little bit of Java: it always has a constructor function. Its name is __new__() and
# is always there for you. When you create an object calling the class name, the first thing Python interpreter
# does is to call __new__() which is liable of allocating a memory space for this object.
# Then, the method __init__() is not exactly the constructor (creator of the object) but only a method
# specified to receive data and initialize an object with that data.
# __new__()  -> intrinsic function responsible for create a nude object;
# __init__() -> up-to-programmer function responsible to initialize the object (referred to as 'self', which
# is another proof that the object was already created).
print(type(my_account))  # <class 'account.Account'>
# As Python is a dynamic language, you can create attributes to an object during runtime.
my_account.balance = 10000
my_account.owner = "James Smith"
print(my_account)  # Memory address of this object.
print(f"Owner: {my_account.owner}\nCurrent balance: ${my_account.balance}")