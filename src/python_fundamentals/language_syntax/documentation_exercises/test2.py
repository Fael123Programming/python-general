def test1():
    for n in range(2, 1000):
        for x in range(2, n):
            if n % x == 0:  # That is, if n is dividable by x!
                print(n, 'equals', x, '*', n // x)
                break
        else:  # This else block is reached if the loop is terminated by exhaustion of the iterable
            # or if the logic condition becomes false.
            # Otherwise, if the loop is interrupted by a break statement this block is not reached.
            print(n, 'is a prime number')


def test2():
    opt = input()
    while opt != "stop":
        opt = input()
        if opt == "do not go into the else statement":
            break  # The else below does not get executed if the logic condition above is evaluated as true.
    else:  # If no break occurs inside the while above the following else gets executed.
        print("Stopped...")


def test3():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)


if __name__ == "__main__":
    test2()
