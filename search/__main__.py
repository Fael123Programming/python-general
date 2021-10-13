from binarySearch import binarySearch
from sequentialSearch import sequentialSearch
from insertionSort import *
from random import randint

listData = list()
for counter in range(1000000):  # Generating a million of random numbers.
    listData.append(randint(0, 1000000))
insertionSort(listData)  # All values are sorted in an increasing way.
print("-- SEARCH VALUES --".center(100, "-"))
opt = int(input("1 - See all generated values\n2 - Search for a number\n3 - Exit\n-> "))
while True:
    while not opt in [1, 2, 3]:
        print("Invalid command")
        print("-- SEARCH VALUES --".center(100, "-"))
        opt = int(input("1 - See all generated values\n2 - Search for a number\n3 - Exit\n-> "))
    if opt == 1:
        print("".center(150, "-"))
        print(listData)
        print("".center(150, "-"))
    elif opt == 2:
        num = int(input("Number in range (0 - 1000000): "))
        while num < 0:
            print(f"{num} is out of range.")
            num = int(input("Number in ranger (0 - 1000000): "))
        srch = int(input("1 - binary search\n2 - sequential search\n-> "))
        while not srch in [1, 2]:
            print("Invalid command")
            srch = int(input("1 - binary search\n2 - sequential search\n-> "))
        if srch == 1:
            position = binarySearch(listData, num)
        else:
            position = sequentialSearch(listData, num)
        if position == -1:
            print(f"{num} was not found.")
        else:
            print(f"{num} was found in position {position}.")
    elif opt == 3:
        exit(0)
    else:
        print("Invalid command")
    print("-- SEARCH VALUES --".center(100, "-"))
    opt = int(input("1 - See all generated values\n2 - Search for a number\n3 - Exit\n-> "))



