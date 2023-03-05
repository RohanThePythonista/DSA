import random
import sys


def find_first_three_max(arr):
    first = -sys.maxsize
    second = first
    third = first
    if len(arr) < 3:
        return
    for val in arr:
        if val > first:
            third = second
            second = first
            first = val
        elif val > second:
            third = second
            second = val
        elif val > third:
            third = val
    print("first:{}".format(first))
    print("second:{}".format(second))
    print("third:{}".format(third))


if __name__ == "__main__":
    input_array = [random.randrange(1, 50, 1) for i in range(10)]
    print("Input array:{}".format(input_array))
    find_first_three_max(input_array)
