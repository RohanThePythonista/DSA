"""
Find max of sum with window size
"""


def get_find_max_sum_of_window_with_size_k(arr, k):
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    max_sum = curr_sum
    for i in range(k, len(arr), 1):
        curr_sum += (arr[i] - arr[i - k])
        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum


if __name__ == '__main__':
    array = [1, 8, 30, -5, 20, 7]
    # array = [100, 8, 30, -5, 20, 7]
    print(get_find_max_sum_of_window_with_size_k(array, 3))
