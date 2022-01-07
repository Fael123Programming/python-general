from timeit import timeit
from src.python_fundamentals.search_techniques import sequential_search as ss
from src.python_fundamentals.search_techniques import binary_search as bs


if __name__ == "__main__":
    data = list(range(1, 1000001, 1))  # 1 to 100,000,000 million
    print("-" * 100)
    print("Sequential python-fundamentals".center(100))
    print("-" * 100)
    lastSecs = timeit(f"ss.sequential_search({data}, 1000000)", "from src.python_fundamentals.search_techniques import sequential_search as ss", number=1)
    print("Worse case: last element or greater than it - Time spent (in seconds):", lastSecs, "- Position:",ss.sequential_search(data, 1000000))
    firstSecs = timeit(f"ss.sequential_search({data}, 1)", "from src.python_fundamentals.search_techniques import sequential_search as ss", number=1)
    print("Best case: first element - Time spent (in seconds):", firstSecs, "- Position:",ss.sequential_search(data, 1))
    print("-" * 100)
    print("Binary python-fundamentals".center(100))
    print("-" * 100)
    firstSecs = timeit(f"bs.binary_search({data}, 0)", "from src.python_fundamentals.search_techniques import binary_search as bs", number=1)
    lastSecs = timeit(f"bs.binary_search({data}, 1000000)", "from src.python_fundamentals.search_techniques import binary_search as bs", number=1)
    print("Worse cases: first element - Time spent (in seconds):", firstSecs, " - Position:", bs.binary_search(data, 1))
    print("Worse cases: last element - Time spent (in seconds):", lastSecs, " - Position:",bs.binary_search(data, 1000000))
    midSecs = timeit(f"bs.binary_search({data}, 500000)", "from src.python_fundamentals.search_techniques import binary_search as bs", number=1)
    print("Best case: element in the middle of our data - Time spent (in seconds):", midSecs, " - Position:",bs.binary_search(data, 500000))
