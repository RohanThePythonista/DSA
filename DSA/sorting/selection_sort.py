"""
O(n^2)
selection sort:
    in each pass it selects min value index
    and swaps with curr picked element
    -it requires max. O(n) swaps

"""


def selection_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = i + 1
        min_value_index = i
        while j < n:
            if arr[j] < arr[min_value_index]:
                min_value_index = j
            j += 1
        arr[min_value_index], arr[i] = arr[i], arr[min_value_index]
        i += 1
    return arr


if __name__ == '__main__':
    from template import template

    array = template.get_random_array(10, 50, 100)
    print(selection_sort(array))
