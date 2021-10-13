def binarySearch(listData: list, data: int):
    low = 0  # First position of the list.
    high = len(listData) - 1  # Last position of the list.
    while low <= high:
        mid = (low + high) // 2
        if listData[mid] == data:  # If the wanted element is in the middle of the list.
            return mid
        elif data < listData[mid]:  # If the wanted element is less than the element in the middle of the list we have
            high = mid - 1  # to search for it from position 0 toward mid - 1.
        else:  # If the wanted element is greater than the element in the middle of the list we
            low = mid + 1  # have to search for it from position mid + 1 toward len(listData) - 1.
    return -1  # Then, if through all repetitions of the while statement above the first if is not evaluated as True, we
    # will get here because low will be greater than high. This condition means that data does not exist in listData.
