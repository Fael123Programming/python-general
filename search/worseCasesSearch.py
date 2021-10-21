from timeit import timeit
from searchTechniques import *

data = list(range(1, 100000001, 1))  # 1 to 100,000,000 million
print("-" * 100)
print("Sequential search".center(100))
print("-" * 100)
seconds = timeit(f"sequentialSearch({data}, 100000000)", "from searchTechniques import sequentialSearch", number=1)
print("Worse case: last element or greater - Time spent (in seconds):", seconds, "- Position:", sequentialSearch(data, 100000000))
seconds = timeit(f"sequentialSearch({data}, 1)", "from searchTechniques import sequentialSearch", number=1)
print("Best case: first element - Time spent (in seconds):", seconds, "- Position:", sequentialSearch(data, 1))
print("-" * 100)
'''
print("Binary search".center(100))
print("-" * 100)
seconds = timeit(f"binarySearch({data}, 0)", "from searchTechniques import binarySearch", number=1)
seconds2 = timeit(f"binarySearch({data}, 1000001)", "from searchTechniques import binarySearch", number=1)
print("Worse case: looking for an element less than or equal to the first element or greater than or equal to the last")
print("element would spend", seconds, "for the first case and", seconds2, "for the second case.")
print("Their position would be, respectively, ", binarySearch(data, 0), "and", binarySearch(data, 1000001))
seconds = timeit(f"binarySearch({data}, 500000)", "from searchTechniques import binarySearch", number=1)
print("Best case: looking for the element in the middle of our data would spend", seconds, "seconds")
print("Its position:", binarySearch(data, 500000))
print("-" * 100)'''
