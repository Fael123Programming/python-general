from timeit import timeit
from searchTechniques.binarySearch import binarySearch
from searchTechniques.linearSearch import sequentialSearch

data = list(range(1, 1000001, 1))  # 1 to 100,000,000 million
print("-" * 100)
print("Sequential search".center(100))
print("-" * 100)
lastSecs = timeit(f"sequentialSearch({data}, 1000000)", "from searchTechniques import sequentialSearch", number=1)
print("Worse case: last element or greater than it - Time spent (in seconds):", lastSecs, "- Position:", sequentialSearch(data, 1000000))
firstSecs = timeit(f"sequentialSearch({data}, 1)", "from searchTechniques import sequentialSearch", number=1)
print("Best case: first element - Time spent (in seconds):", firstSecs, "- Position:", sequentialSearch(data, 1))
print("-" * 100)
print("Binary search".center(100))
print("-" * 100)
firstSecs = timeit(f"binarySearch({data}, 0)", "from searchTechniques import binarySearch", number=1)
lastSecs = timeit(f"binarySearch({data}, 1000000)", "from searchTechniques import binarySearch", number=1)
print("Worse cases: first element - Time spent (in seconds):", firstSecs, " - Position:", binarySearch(data, 1))
print("Worse cases: last element - Time spent (in seconds):", lastSecs, " - Position:", binarySearch(data, 1000000))
midSecs = timeit(f"binarySearch({data}, 500000)", "from searchTechniques import binarySearch", number=1)
print("Best case: element in the middle of our data - Time spent (in seconds):", midSecs, " - Position:", binarySearch(data, 500000))
