"""
Given an array with repeated elements thrice but only element is non-repeated
Find that non-repeated element
For only sorted array input:
            using curr element and its second next ele to compare and check if they matches
            keep traversing from i to n
                if i < n-2 and arr[i] != arr[i+2]:
                    found non-repeated element
                i += 3

For unsorted and sorted array:
    Using aux space array with size of know max no. in input array with default values 0
    copy input array to new array
    Traverse new array:
    Use index of elements to mark them as visited
        if array[abs(arr[i]) >=0:
            # calculate sum of elements considering all are repeated
            sum_with_repeated_marked = sum_with_repeated_marked + abs(array[i]) * 3
            # mark this element as visited by making its occurrence as negative
            array[abs(array[i])] *= -1
    now again traverse array to get actual sum with non-repeated ele
            if array[i] < 0:
                array[i] = -1 * array[i]
            sum_with_repeated_marked = sum_with_repeated_marked - array[i]
    result = sum_with_repeated_marked//2

Pythonic way:
    Using set:
        repeated_sum = sum(set(array)) * 3
        normal_sum = sum(array)
        non_repeated_ele =  (repeated_sum - normal_sum)//2
"""


def find_non_repeated_in_sorted_array(array):
    n = len(array)
    if n < 3:
        print("invalid input, please check once again with more than or equal to 3 elements")
        return
    i = 0
    while i < n:
        if i < n - 2 and array[i] != array[i + 2]:
            print("non_repeated:{}".format(array[i]))
            break
        i += 3
    else:
        repeated = -1 if array[n - 3] == array[n - 1] else array[n - 1]
        print("non_repeated:{}".format(repeated))


def find_non_repeated_unsorted(array):
    i = 0
    n = len(array)
    sum_with_repeated_marked = 0
    while i < n:
        if array[abs(array[i])] >= 0:
            sum_with_repeated_marked = sum_with_repeated_marked + abs(array[i]) * 3
            array[abs(array[i])] *= -1
        i += 1
    print(sum_with_repeated_marked)
    print(array)
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = -1 * array[i]
        sum_with_repeated_marked = sum_with_repeated_marked - array[i]
    print(sum_with_repeated_marked)
    print("non_repeated:{}".format(sum_with_repeated_marked >> 1))


def pythonist_solution(array):
    repeated_sum = sum(set(array)) * 3
    normal_sum = sum(array)
    print("non_repeated:{}".format((repeated_sum - normal_sum) >> 1))


if __name__ == '__main__':
    a = [0, 1, 0, 1, 0, 1, 99]
    nums = [0 for _ in range(max(a) + 1)]
    for i in range(len(a)):
        nums[i] = a[i]
    find_non_repeated_in_sorted_array(a)
    find_non_repeated_unsorted(nums)
    pythonist_solution(a)
