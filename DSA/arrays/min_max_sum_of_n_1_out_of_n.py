"""
Find minimum and maximum sum of n-1 elements out of n elements from array
Assume all are positive no, in an array
Method 1:
    Find max and min from array and sum of all array elements
    then
        max_sum = array_sum - min_ele
        min_sum = array_sum - max_ele
    This solution works for negative ele also
    TC: O(n)
    SC: O(1)

Method2 2:
    Using aux space for prefix sum array
    Crate prefix sum array and then after use last ele of prefix sum array
    to find min and max sum of n-1 ele of input array
    min = MAX
    max = -MAX
    Traverse input array:
        keep track of curr_min and curr_max
            using prefix_sum_array[end] - curr_val
        compare them with min and MAX and update
    TC: O(n)
    SC: O(n)
"""
import sys


def miniMaxSum(arr):
    prefix_sum_array = get_prefix_sum_array(arr)
    min_sum = sys.maxsize
    max_sum = -sys.maxsize
    for val in arr:
        t_min_sum = prefix_sum_array[-1] - val
        t_max_sum = prefix_sum_array[-1] - val
        if t_min_sum < min_sum:
            min_sum = t_min_sum
        if t_max_sum > max_sum:
            max_sum = t_max_sum
    print(min_sum, max_sum)


def get_prefix_sum_array(array):
    sum_array = list()
    sum_var = 0
    for i in array:
        sum_var += i
        sum_array.append(sum_var)
    return sum_array


if __name__ == '__main__':
    """
    https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
    One approach could be find max and min from array and array ele sum...and then max_sum = array_sum - min_ele and min_sum = array_sum - max_ele
    other approach to use prefix sum array
    """
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
