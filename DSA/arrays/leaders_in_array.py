"""
Find leaders in an array
printing all leaders means after current element there is no other bigger element
e.g. i/p array:[87, 76, 83, 88, 88, 37, 92, 70, 64, 41]
leaders ---->64 70 92 41

Method 1: Naive approach
    Use two loops
    For each element index i travers i+1 to n:
        and check there is no greater ele than it
    TC:O(n^2)
    SC:O(1)

Method 3: Efficient solution
    Traverse input array in reverse direction
    Last ele is always leader-->make it curr max
    Traverse from second last ele to first
        check if curr ele is > curr_max
            update curr max = curr ele
            print curr max ele
    TC: O(n)
    SC:O(1)
"""
from DSA.arrays.input_header import input_array


def print_leaders(arr):
    print("i/p array:{}".format(arr))
    max_val = arr[-1]
    for i in range(-2, -len(arr) - 1, -1):
        if arr[i] > max_val:
            max_val = arr[i]
            print(max_val, end=" ")
    print(arr[-1])


if __name__ == '__main__':
    print_leaders(input_array)
