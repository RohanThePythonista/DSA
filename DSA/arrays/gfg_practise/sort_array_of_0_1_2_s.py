from DSA.template.template import *


def sort_array(arr):
    low, mid = 0, 0
    high = len(arr) - 1
    i = 0
    while i < len(arr):
        if array[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
        i += 1


if __name__ == '__main__':
    # array = get_random_array(10, 0, 3)
    # print(array)
    # sort_array(array)
    # print(array)
    test_cases = int(input())
    for t_case in range(test_cases):
        n = map(int, input().split())
        array = list(map(int, input().split()))
        sort_array(array)
        for val in array:
            print(val, end=" ")
        print('')