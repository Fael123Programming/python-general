def insertionSort(listData: list, increasingOrder=True):
    if increasingOrder:  # Ordering in an increasing order.
        for j in range(1, len(listData)):
            value = listData[j]
            i = j - 1
            while i >= 0 and listData[i] > value:  # a previous is greater than a next?
                listData[i + 1] = listData[i]  # shift them!
                i -= 1
            listData[i + 1] = value
    else:  # Ordering in a decreasing order.
        for j in range(1, len(listData)):
            value = listData[j]
            i = j - 1
            while i >= 0 and listData[i] < value:
                listData[i + 1] = listData[i]
                i -= 1
            listData[i + 1] = value


def binaryInsertionSort(listData):
    from searchTechniques.binarySearch import binarySearchPossible2
    for i in range(1, len(listData)):
        key = listData[i]
        if listData[i - 1] != key:
            listData.remove(key)
            listData.insert(binarySearchPossible2(listData, key, 0, i - 1), key)
