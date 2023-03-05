from DSA.arrays.template import get_random_array


def find_max(input_arr):
    """
    This is better approach
    TC: O(n)
    SC:O(1)
    Idea is to decide max of curr_sum and curr_ele while traversing array
        For curr_sum add curr_ele to it and compare with curr_ele
        then update curr_sum as max of this comparison
    :param input_arr:
    :return:
    """
    curr_max = max_sum = input_arr[0]
    i = 1
    while i < len(input_arr):
        curr_max = max(curr_max + input_arr[i], input_arr[i])
        if curr_max >= max_sum:
            max_sum = curr_max
        i += 1
    print(max_sum)


if __name__ == '__main__':
    input_array = get_random_array(10, -5, 10)
    find_max(input_array)
