from template.template import get_sequence_list, get_random_array


def search(arr, key):
    left = arr[0]  # left starting index
    right = arr[-1]  # right index
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            print("key:{} at index:{}".format(key, mid))
            return
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print("key is not present in array")


def recursive_search(arr, left, right, key):
    if left > right:
        print("key is not present in array")
        return
    mid = (left + right) // 2
    if arr[mid] == key:
        print("key:{} at index:{}".format(key, mid))
        return mid
    elif key < arr[mid]:
        return recursive_search(arr, left, mid - 1, key)
    return recursive_search(arr, mid + 1, right, key)


if __name__ == '__main__':
    input_array = get_sequence_list(100)
    search(input_array, 0)
    print(recursive_search(input_array, 0, len(input_array), 1909))
