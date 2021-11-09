def sequentialSearch(listData: list, data: int):
    i = 0
    while i < len(listData) and listData[i] < data:
        i += 1
    if i == len(listData) or listData[i] != data:
        # See that not always when we did not find a value i is n. We are comparing values using '<'.
        return -1  # A default value for when data is not found in listData.
    else:
        return i
