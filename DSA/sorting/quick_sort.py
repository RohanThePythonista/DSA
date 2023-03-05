def partition(arr, low, high):
    pivot = arr[high]
    j = low
    i = low - 1
    while j < high:
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
        j += 1
    swap(arr, i + 1, high)
    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


if __name__ == '__main__':
    from template import template

    input_arr = template.get_random_array(10, 30, 80)
    quick_sort(input_arr, 0, len(input_arr)-1)
    print(input_arr)
