from timeit import timeit

numbers = list(range(10000, 0, -1))
seconds = timeit(f"insertionSort({numbers})", "from sortValues import insertionSort", number=1)
print(seconds)
