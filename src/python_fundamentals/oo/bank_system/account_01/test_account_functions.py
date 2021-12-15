import account_functions

acc1 = account_functions.create_account("Rafael Fonseca", "456-99", "YUI/89", 10000)
account_functions.deposit(acc1, 5000)
print("Current data: ", acc1)
account_functions.withdraw(acc1, 3500)
print("Result data:  ", acc1)