"""
Given an array and sum
Check if array has sub_arr with given sum
e.g.
    array = [1, 4, 20, 3, 10, 5],    i_p_sum = 33
    o/p: yes (True)
    --> from index 2 to 4 has sum 33, so sub_arr exists with given sum in arr
Naive approach:O(n^2)
Use two loops:
    for i 0 to n:
        for j=i to n:
            sum += arr[j]
            and keep checking given_sum == sum
                then if exists return True
    return False # if not found

Better approach:O(n)
 To use sliding window technique if array has only positive integers

use two pointers(start, next) from first index(0):
keep calculating sum with next pointer
    while if curr_sum > given_sum:
        then subtract initial values from curr window sum using start pointer
    if at any point given sum found then return True
"""


def is_sub_arr_exists_with_given_sum(arr, given_sum):
    curr_sum = 0
    start = 0
    next_ = 0
    while next_ < len(arr):
        curr_sum += arr[next_]
        while curr_sum > given_sum:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == given_sum:
            return True
        next_ += 1
    return False


def get_prefix_sum(arr):
    prefix_sum_arr = []
    pre_sum = 0
    for val in arr:
        pre_sum += val
        prefix_sum_arr.append(pre_sum)
    return prefix_sum_arr


if __name__ == '__main__':
    # array = [1, 4, 20, 3, 10, 5]
    # i_p_sum = 33
    # array = [1, 4, 0, 0, 3, 10, 5]
    # i_p_sum = 7
    array = [2, 3]
    i_p_sum = 4
    print(is_sub_arr_exists_with_given_sum(array, i_p_sum))
