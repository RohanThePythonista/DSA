"""
[1,1,1,5,3,5,5,5,3]
n = 9
o/p: major_elem is more than n//2

expected TC->O(n), SC:O(1) ---> use moore voting algorithm
"""


def find_majority(array):
    """
    Idea is to use nlogn sorting algorithm
    Then iterate over sorted array
        and find no. of occurrences
            (find no. of occurrences takes logn time
            using binary search to find left and right index of element)
         and check if it appears more than n/2 times we found majority element
    This solution works in overall in nlogn time (nologn(sort) + (n(logn+logn)(no. of occurrences)))
    :param array:list, input array
    :return:int, majority element in an array
    """
    n = len(array)
    i = 0
    array = sorted(array)  # nlogn
    majority = -1
    while i < n:  # n
        majority = find_no_of_occurrence_of_key(array, 0, n, array[i])  # logn
        if majority >= n // 2:
            break
        i += 1
    return array[i] if majority != -1 and i != n else -1


def find_no_of_occurrence_of_key(arr, low, high, key):
    """
    It finds leftmost and rightmost index of given key in sorted array
    and returns no. of occurrences of key
    :param arr: list, input array
    :param low: left most index of array
    :param high: right most of array
    :param key: int, key whose no. of occurrences to be find
    :return: int, no. of occurrences of key
    """
    left_most_index = find_left_most_index(arr, low, high, key)
    if left_most_index == -1:
        return -1
    right_most_index = find_right_most_index(arr, low, high, key)
    return right_most_index - left_most_index + 1


def find_left_most_index(arr, low, high, key):
    """
    Idea is to use binary search algorithm to find left most index
    :param arr:list, input array
    :param low:int, leftmost index
    :param high:int, rightmost index
    :param key:int, key whose leftmost index to find in sorted array
    :return:
    """
    while low <= high:
        mid = (low + high) // 2
        # check if mid pos ele is leftmost index
        # means check if mid pos ele is key and mid is either first index or its previous index ele is not key
        if arr[mid] == key and (mid == 0 or arr[mid - 1] != key):
            return mid
        elif arr[mid] >= key:  # this is important
            # go to left sub-array
            high = mid - 1
        else:
            # go to right sub-array
            low = mid + 1
    return -1


def find_right_most_index(arr, low, high, key):
    """
     Idea is to use binary search algorithm to find right most index
     :param arr:list, input array
     :param low:int, leftmost index
     :param high:int, rightmost index
     :param key:int, key whose rightmost index to find in sorted array
     :return:
     """
    while low <= high:
        mid = (low + high) // 2
        # check if mid pos ele is rightmost index
        # means check if mid pos ele is key and mid is either last index or its next index ele is not key
        if arr[mid] == key and (mid == len(arr) - 1 or arr[mid + 1] != key):
            return mid
        elif arr[mid] <= key:  # this is important
            # go to right sub-array
            low = mid + 1
        else:
            # go to left sub-array
            high = mid - 1
    return -1


def majority(array, length):
    """
    https://www.geeksforgeeks.org/majority-element/
    This is moore-voting algorithm
    TC - O(n)
    SC- O(1)
    Idea is to use counter assuming each candidate(ele in arr) is winning candidate(majority ele)
    Assume major_index = 0
    and count = 1
    Traverse an array from 1 to n:
        check if major_index element is equal to curr index element
            increase count += 1
        else:
            decrease count -= 1
        if count becomes zero at any point
            then change major_index to curr index
            and reset count = 1
    Now major_index ele is likely to be winning candidate
    But it requires to assured
        So traverse array once again and
            keep count if major_index index ele in array
                if  count > n/2 then return major index element
    :param array:
    :param length:
    :return:
    """
    count = 1
    i = 1
    major_index = 0
    while i < length:
        if arr[major_index] == array[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            major_index = i
            count = 1
        i += 1
    count = 1
    for val in array:
        if val == array[major_index]:
            count += 1
            pass
        if count >= length // 2:
            return array[major_index]


if __name__ == '__main__':
    print(find_majority([1, 1, 1, 5, 3, 5, 5, 5, 3, 5]))
    # size = 20
    # arr = [-1] * 20
    # for i in [1, 1, 1, 5, 3, 5, 5, 5, 3, 5]:
    #     arr[]
    # arr = [1, 1, 1, 5, 3, 5, 5, 5, 3, 5]
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]
    size = len(arr)
    print(majority(arr, size))
