def insertionSort(listData: list):
    for j in range(1, len(listData)):
        value = listData[j]
        i = j - 1
        while i >= 0 and listData[i] > value:  # a previous is greater than a next?
            listData[i + 1] = listData[i]  # shift them!
            i -= 1
        listData[i + 1] = value
