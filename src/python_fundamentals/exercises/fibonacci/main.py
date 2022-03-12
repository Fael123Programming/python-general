def calculate_fib(max_numbers: int):
    assert max_numbers > 0, f"max_numbers {max_numbers} must be > 0"
    a, b = 0, 1
    while max_numbers > 0:
        print(a, end="")
        a, b = b, a+b
        if max_numbers > 1:
            print(end=", ")
        max_numbers -= 1


if __name__ == "__main__":
    calculate_fib(0)
