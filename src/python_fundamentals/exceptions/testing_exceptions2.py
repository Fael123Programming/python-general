if __name__ == "__main__":
    n1 = int(input("First number: "))
    n2 = int(input("Second number: "))
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"{n1} / {n2} = {result}")
    try:
        with open("/home/leafar/documents/prg/code/py/python-general/src/python_fundamentals/exceptions/account.py", "r") as file:
            print(f"File opened:")
            for i in file.readlines():
                i = i.replace("\n", "")
                print(i)
    except IOError:
        print("IOError has been raised")
