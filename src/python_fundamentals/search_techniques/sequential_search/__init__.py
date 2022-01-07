def sequential_search(list_data: list, data: int):
    i = 0
    while i < len(list_data) and list_data[i] < data:
        i += 1
    if i == len(list_data) or list_data[i] != data:
        # See that not always when we did not find a value i is n. We are comparing values using '<'.
        return -1  # A default value for when data is not found in listData.
    else:
        return i
