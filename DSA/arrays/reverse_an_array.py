from DSA.arrays.input_header import input_array


def iterative_reverse(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        arr[j], arr[i] = arr[i], arr[j]
        i += 1
        j -= 1
    print("iterative_reverse array:{}".format(arr))


def recursive_reverse(arr, start, end):
    if start >= end:
        print("recursive_reverse array:{}".format(arr))
        return
    arr[end], arr[start] = arr[start], arr[end]
    start += 1
    end -= 1
    recursive_reverse(arr, start, end)


if __name__ == '__main__':
    iterative_reverse(input_array)
    print("i/p arr:{}".format(input_array))
    recursive_reverse(input_array, 0, len(input_array)-1)
