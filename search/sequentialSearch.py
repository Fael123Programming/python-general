def sequentialSearch(listData: list, data: int):
    i = 0
    while i < len(listData) and listData[i] < data:
        i += 1
    if i == len(listData) or listData[i] != data:
        return -1
    else:
        return i
