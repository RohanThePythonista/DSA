import random


def get_sequence_list(n):
    input_list = [i for i in range(n + 1)]
    print("input list:{}".format(input_list))
    return input_list


def get_random_array(n, from_, to_):
    input_array = [random.randrange(from_, to_, 1) for i in range(n)]
    print("input arr:{}".format(input_array))
    return input_array


def create_prefix_sum_array(array):
    sum_var = 0
    prefix_sum_array = list()
    for val in array:
        sum_var += val
        prefix_sum_array.append(sum_var)
    print("prefix_sum_array:{}".format(prefix_sum_array))
    return prefix_sum_array


if __name__ == '__main__':
    pass
