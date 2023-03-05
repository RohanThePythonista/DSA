def partition(arr, low, high):
    pivot = arr[high]
    curr_low = low
    prev_low_to_swap = low - 1
    while curr_low < high:
        if arr[curr_low] <= pivot:
            prev_low_to_swap += 1
            arr[curr_low], arr[prev_low_to_swap] = arr[prev_low_to_swap], arr[curr_low]
        curr_low += 1
    arr[prev_low_to_swap+1], arr[high] = arr[high], arr[prev_low_to_swap + 1]
    return prev_low_to_swap + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


if __name__ == '__main__':
    from practise.template import template

    array = template.get_random_array(10, -20, 20)
    quick_sort(array, 0, len(array) - 1)
    print(array)
