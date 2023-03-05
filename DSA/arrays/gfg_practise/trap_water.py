"""
given arr of integer inputs, find max water that can be trapped
consider elements as blocks in array
e.g
i/p arr = [2, 0, 2]
o/p = total 2 units of water can be trapped

i/p arr = [3, 0, 1, 2, 5]
o/p = 6 units of total water

Naive approach: O(n^2)

At each index find maximum at its left and right
    take min of these two maximums and subtract current value from it
        and keep adding above values found
    res = 0
    summation i = 0 to n
        res += min(l_max, r_max) - arr[i]
    return res

better approach is using aux space for storing left max and right max for each ele in i/p array
    ->TC = O(n), SC = O(n)
    Idea is to crate left and right max arrays for each ele of i/p arr
        then use res += min(left, right) - 1

Space Optimization:O(1)
Instead of maintaining two arrays of size n for storing left and right max of each element,
    maintain two variables to store the maximum till that point.
    Since water trapped at any
        element = min(max_left, max_right) – arr[i].
        Calculate water trapped on smaller element out of arr[start] and arr[end] first
        and move the pointers till start doesn't cross end.

"""


def get_trap_water_units(array):
    n = len(array)
    if n < 3:
        print(f"len:{n} is not valid it should be at least 3")
        return 0
    result = 0
    l_max = get_left_max_arr(array)
    print(l_max)
    r_max = get_right_max_arr(array)
    print(r_max)
    for i in range(n):
        result = result + min(l_max[i], r_max[i]) - array[i]
    return result


def get_left_max_arr(array):
    n = len(array)
    print(f"len:{n}")
    arr = [0] * n
    curr_max = array[0]
    arr[0] = curr_max
    for i, val in enumerate(array):
        if i == n - 1 or val > curr_max:
            arr[i] = val
            curr_max = arr[i]
        else:
            arr[i] = curr_max
    return arr


def get_right_max_arr(array):
    n = len(array)
    print(f"len:{n}")
    arr = [0] * n
    arr[n - 1] = array[n - 1]
    curr_max = arr[n - 1]
    for i in range(n - 1, -1, -1):
        if array[i] > curr_max:
            arr[i] = array[i]
            curr_max = arr[i]
        else:
            arr[i] = curr_max
    return arr


def trap_water_calculate(array):
    n = len(array)
    if n < 3:
        return 0
    start = 0
    end = n - 1
    l_max = 0
    r_max = 0
    result = 0
    while start <= end:
        if array[start] < array[end]:
            if array[start] > l_max:
                l_max = array[start]
            else:
                result += l_max - array[start]
            start += 1
        else:
            if array[end] > r_max:
                r_max = array[end]
            else:
                result += r_max - array[end]
            end -= 1
    return result


if __name__ == '__main__':
    input_arr = [3, 0, 1, 2, 5]
    # input_arr = [2, 0, 2]
    # print(get_trap_water_units(input_arr))
    print(trap_water_calculate(input_arr))
