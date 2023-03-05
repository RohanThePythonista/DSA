"""
Sliding window technique
it is traversing over k elements at a time
    -->let say we have window of k elements
        ->then while traversing
            we add next ele of kth ele to curr window and exclude first ele
"""

from DSA.arrays.input_header import input_array, input_list


def find_max_sum_of_k_consecutive_elements(arr, window_size):
    # naive approach
    max_sum = 0
    i = 0
    while i < len(arr):
        sum_of_k = sum(arr[i:window_size + i])
        if sum_of_k > max_sum:
            max_sum = sum_of_k
        i += 1
    print("max_sum:{} ".format(max_sum))


def find_max_sum_of_k_elements(arr, k):
    # better approach using sliding window technique
    max_sum = sum(arr[0:k])  # store sum of first k ele from input array
    i = 1
    while i <= len(arr) - k:
        # slide to next window, drop first ele from curr window and add next ele from array to curr window
        new_sum = max_sum - arr[i - 1] + arr[i + k - 1]
        if max_sum < new_sum:
            max_sum = new_sum
        i += 1
    print("max_sum:{} ".format(max_sum))


if __name__ == '__main__':
    find_max_sum_of_k_consecutive_elements(input_list, 3)
    find_max_sum_of_k_elements(input_list, 3)
