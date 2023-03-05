def reverse_arr_in_groups(arr, k, n):
    i = 0
    while i < n:
        j = i
        i += k
        arr[j:i] = reversed(arr[j:i])


if __name__ == '__main__':
    # array = [10, 20, 30, 40, 50, 60]
    # reverse_arr_in_groups(array, 2, len(array))
    test_cases = int(input())
    for t_case in range(test_cases):
        n, k = tuple(map(int, input().split()))
        array = list(map(int, input().split()))
        reverse_arr_in_groups(array, k, n)
        for val in array:
            print(val, end=" ")
        print('')
