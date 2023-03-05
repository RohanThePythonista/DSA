from DSA.template.template import *


def get_sub_arr_with_given_sum(array, input_sum):
    start_index = 0
    end_index = -1
    curr_sum = 0
    for i, val in enumerate(array):
        if curr_sum < input_sum:
            curr_sum += val
            end_index += 1
        if curr_sum > input_sum:
            while curr_sum > input_sum:
                curr_sum -= array[start_index]
                start_index += 1
        if curr_sum == input_sum:
            return start_index, end_index
    return -1


if __name__ == '__main__':
    test_cases = int(input())
    for t_case in range(test_cases):
        n, sum_given = tuple(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(get_sub_arr_with_given_sum(arr, sum_given))
    # arr = [1, 2, 3, 7, 5]
    # ip_sum = 18
