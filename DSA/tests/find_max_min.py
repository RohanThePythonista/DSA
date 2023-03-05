
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9.1]


def find_max_min(test_array):
    return max(test_array), min(test_array)


def find_max_value(test_array):
    for index, val in enumerate(test_array):
        print(index, val)


if __name__ == '__main__':
    print(find_max_min(test_list))

