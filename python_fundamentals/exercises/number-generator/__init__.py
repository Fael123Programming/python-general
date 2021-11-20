from searchTechniques.binarySearch import binarySearch
from searchTechniques.linearSearch import sequentialSearch
from sortMethods.insertionSort import insertionSort
from random import randint

while True:
    print("-- SEARCH VALUES --".center(100, "-"))
    quantity = input("How many numbers to generate randomly? ")
    if not quantity.isnumeric():
        print("Invalid input")
    else:
        break
listData = list()
for counter in range(int(quantity)):  # Generating 'quantity' random numbers.
    listData.append(randint(0, 1000000))  # 0 - 1000000 is the applied range.
insertionSort(listData)  # All values are sorted in an increasing way.
while True:
    print("-- SEARCH VALUES --".center(100, "-"))
    opt = input("1 - See all generated values\n2 - Search for a number\n3 - Exit\n-> ")
    if opt == "1":
        print("".center(150, "-"))
        c = 0
        for data in listData:
            print(data, end=" ")
            c += 1
            if c == 50:
                print()
                c = 0
    elif opt == "2":
        while True:
            num = input("Number in range (0 - 1000000): ")
            if not num.isnumeric():
                print("Invalid input")
            else:
                break
        srch = input("1 - binary python-fundamentals\n2 - sequential python-fundamentals\n-> ")
        while srch != "1" and srch != "2":
            print("Invalid command")
            srch = input("1 - binary python-fundamentals\n2 - sequential python-fundamentals\n-> ")
        if srch == "1":
            position = binarySearch(listData, int(num))
        else:
            position = sequentialSearch(listData, int(num))
        if position == -1:
            print(f"{num} was not found.")
        else:
            print(f"{num} was found in position {position}.")
    elif opt == "3":
        exit(0)
    else:
        print("Invalid command")
