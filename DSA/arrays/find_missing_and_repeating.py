"""
Given an unsorted array of size n. Array elements are in the range from 1 to n.
One number from set {1, 2, …n} is missing and one number occurs twice in the array.
Find these two numbers.

Method 1:
    Using sorting
        1.Sort the input array.
        2.Traverse the array and check for missing and repeating.
    TC: O(nLogn)

Method 2:
    Using aux count array
        1. Create an array temp[] of size n with all default values 0.
        2. Traverse the input array arr[], and do following for each arr[i]
            if(temp[arr[i]] == 0)
                temp[arr[i]] = 1;
            if(temp[arr[i]] == 1)
                update repeating = arr[i] # output
        3.Traverse temp[] and output the array index having value as 0
            (This is the missing element) # output
    TC: O(n)
    SC: O(n)

Method 3:
    Using array elements as index and mark the visited places
    Traverse the array.
    While traversing,
        use the absolute value of every element as an index
            and make the value at this index as negative to mark it visited.
        If something is already marked negative then this is the repeating element.
        To find missing, traverse the array again and look for a positive value.
    TC: O(n)
    SC:O(1)

Method 4:
    TC:O(n)
    SC:O(1)
    Using formula:
    for val in array:
        sum_n += val
        sum_n_square += val * val
    x = (n * (n + 1)) // 2 - sum_n  # sum(1 to n) - actual sum
    y = ((n * (n + 1) * (2 * n + 1)) // 6 - sum_n_square) // x   # sum_of_square(1 to n) - actual
    repeat = (y-x)//2
    missing = (x+y)//2
    print("repeat:{} missing:{}".format((y - x) // 2, (x + y) // 2))
"""


def find_missing_and_repeating_using_sort(array):
    array.sort()  # O(nLogn)
    repeat = 0
    missing = 0
    for i, val in enumerate(array):  # O(n)
        if val - 1 != i:
            repeat = val
            missing = i + 1
    print('repeat:{}, missing:{}'.format(repeat, missing))


def find_missing_and_repeating_using_count_array(array):
    # method 2
    n = len(array)
    temp = [0 for _ in range(n)]  # aux count array
    repeat = 0
    for i in array:
        # array values would be 1 t0 n only as input
        if temp[i - 1] == 0:
            temp[i - 1] = 1
        elif temp[i - 1] == 1:
            repeat = i
    missing = 0
    for i, val in enumerate(temp):
        if val == 0:
            missing = i + 1
            break
    print('repeat:{}, missing:{}'.format(repeat, missing))


def find_missing_and_repeating_using_indexing(array):
    # method 3
    repeat = 0
    for i in range(len(array)):
        if array[abs(array[i]) - 1] > 0:
            array[abs(array[i]) - 1] *= -1
        else:
            repeat = abs(array[i])
    missing = 0
    for i in range(len(array)):
        if array[i] > 0:
            missing = i + 1
            break
    print("repeat:{}, missing:{}".format(repeat, missing))


def find_missing_and_repeating_using_formula(array):
    # TODO: This solution is not correct
    # method 4
    n = len(array)
    sum_n = 0
    sum_n2 = 0
    for val in array:
        sum_n += val
        sum_n2 += val * val
    x = (n * (n + 1)) // 2 - sum_n
    y = ((n * (n + 1) * (2 * n + 1)) // 6 - sum_n2) // x
    print("repeat:{} missing:{}".format((y - x) // 2, (x + y) // 2))


if __name__ == '__main__':
    arr = [1, 2, 4, 4, 5]
    find_missing_and_repeating_using_sort(arr)
    find_missing_and_repeating_using_count_array(arr)
    find_missing_and_repeating_using_indexing(arr)
    find_missing_and_repeating_using_formula(arr)
