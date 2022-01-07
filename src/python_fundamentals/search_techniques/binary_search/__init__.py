def binary_search(list_data: list, data: int):
    low = 0
    high = len(list_data) - 1
    while low <= high:
        mid = (low + high) // 2  # In the last repetition, low will be equal to high and then, mid will be equal to them
        if list_data[mid] == data:  # If the wanted element is in the middle of the list.
            return mid
        elif data < list_data[mid]:  # If the wanted element is less than the element in the middle of the list we have
            high = mid - 1  # to python-fundamentals for it from position 0 toward mid - 1.
        else:  # If the wanted element is greater than the element in the middle of the list we
            low = mid + 1  # have to python-fundamentals for it from position mid + 1 toward len(listData) - 1.
    return -1  # Then, if through all repetitions of the while statement above the first if is not evaluated as True, we
    # will get here because low will be greater than high. This condition means that data does not exist in listData.


def binary_search_possible(list_data, data):
    low = 0
    high = len(list_data) - 1
    while low <= high:
        mid = (low + high) // 2
        if list_data[mid] == data:
            return mid
        if list_data[mid] < data:
            low = mid + 1
        else:
            high = mid - 1
    return low


def binary_search_possible2(list_data, data, from_pos, to_pos):
    low = from_pos
    high = to_pos
    while low <= high:
        mid = (low + high) // 2
        if list_data[mid] == data:
            return mid
        if list_data[mid] < data:
            low = mid + 1
        else:
            high = mid - 1
    return low

