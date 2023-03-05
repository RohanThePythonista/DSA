def bubble_sort(arr):
    """
    with each pass max value pushed to its position
    :param arr:
    :return:
    """
    for i in range(len(array)):
        j = 0
        while j < len(arr) - i - 1:  # we don't consider last ele once it is at its correct pos
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        print(arr)
    print(arr)


def insertion_sort(arr):
    """
    with each pass a key will be inserted to its sorted position
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while key < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    print(arr)


def selection_sort(arr):
    """
    with each pass min value will be put at its appropriate position
    :param arr:
    :return:
    """
    for i in range(len(arr) - 1):
        i_min = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[i_min]:
                i_min = j  # get index of min value than current value
            j += 1
        arr[i], arr[i_min] = arr[i_min], arr[i]  # put min at its pos
        print(arr)
    print(arr)


def partition(arr, low, high):
    pass


def quick_sort(arr, low, high):
    pass


if __name__ == '__main__':
    array = [5, 4, 3, 2, 1, 0]
    bubble_sort(array)
    print("\n")
    array = [5, 4, 3, 2, 1, 0]
    insertion_sort(array)
    print("\n")
    array = [5, 4, 3, 2, 1, 0]
    selection_sort(array)
