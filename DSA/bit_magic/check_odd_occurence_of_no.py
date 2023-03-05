input_list = [2, 2, 4, 4, 3]


def find_odd_occurrence(arr):
    res = 0
    for val in arr:
        res = val ^ res
    print(res)


if __name__ == '__main__':
    find_odd_occurrence(input_list)
