"""
Find first and last index of repeated no. in sorted array of 1 to n-1.  O(Logn)
Only no. is repeated twice in given input array
e.g input_array = [1,2,3,4,4]
    output = 4
    input_arr = [1,1,2,3,4]
    output = 1

Method 1: Naive approach
    Traverse whole array and check if curr ele is repeated
    TC:O(n)

Method 2: Best solution
    Idea is to use binary search
    1- Check if the middle element is the repeating one.
    2- If not then check if the middle element is at proper position if yes then start searching repeating element in right.
    3- Otherwise the repeating one will be in left.

    TC:O(Logn)
"""


def get_repeated_in_sorted_array(array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        # check if middle ele is repeated one
        if 0 < mid < len(array) and (array[mid] == array[mid - 1] or array[mid] == array[mid + 1]):
            return array[mid]
        if array[mid] == mid + 1:
            # if mid is at its proper position then repeated ele should be in right half of the array
            start = mid + 1
        else:
            # else repeated should be in left half of the array
            end = mid - 1
    return -1


if __name__ == '__main__':
    # input_array = [1, 2, 3, 4, 4]
    input_array = [1, 1, 2, 3, 4]
    print(get_repeated_in_sorted_array(input_array))
