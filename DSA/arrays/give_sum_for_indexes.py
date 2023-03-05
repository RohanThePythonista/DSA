"""
Prefix sum array concept:
This array basically stores the sum till curr index of input array
to that index in it.
e.g input_array = [1,2,3,4,5]
prefix_sum_array = [1,3,6,10,15]
"""

from DSA.arrays.template import *


def create_array(n):
    global prefix_sum_array
    input_arr = get_sequence_list(n)
    prefix_sum_array = create_prefix_sum_array(input_arr)


def give_sum(start_index, end_index):
    """
    Finding sum of elements between start and end indexes of given array
    If we create prefix sum array to find result of such multiple queries
    it would be efficient
    using this approach it require O(n) extra space and O(n) processing only initially
     result = prefix_sum_array[end_index] - prefix_sum_array[start_index - 1]
    :param start_index:
    :param end_index:
    :return:
    """
    if start_index == 0:
        return prefix_sum_array[end_index]
    return prefix_sum_array[end_index] - prefix_sum_array[start_index - 1]


if __name__ == '__main__':
    create_array(10)
    print(give_sum(1, 4))
