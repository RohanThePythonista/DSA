def check_sorted_array_rotated(array):
    low = 0
    high = len(array) - 1
    if array[low] > array[low + 1]:
        return 1
    elif array[high] < array[high - 1]:
        return high
    low = 1
    high -= 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < array[mid - 1]:
            return mid
        elif array[mid] > array[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


"""
123456
6712345
"""

if __name__ == '__main__':
    input_arry = [6, 7, 8, 1, 2, 3, 4, 5]
    print(check_sorted_array_rotated(input_arry))
