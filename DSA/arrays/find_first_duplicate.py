"""
Given an array. array elements are between 1 to len of array.
Array elements may have duplicates. You have to find first duplicate in array.

Method 1:Naive approach
    Use two loops and keep track of index of duplicate
    first_duplicate_index = 0
    for each ele i:
        for each j=i+1 to n:
            check if arr[j] is equal to arr[i]
              first_duplicate_index = min(first_duplicate_index, j)
    TC:O(n^2)
    SC:O(1)

Method 2:
    Using map as look up table
    create a dict like seen = dict()
    travers and array:
        if ele is seen:
            return ele
        else:
            add this ele to seen dict
            seen[ele] = i
    TC: O(n)
    SC:O(n)

Method 3: Best solution
    Use given information -->IMP
        -->array ele values are between 1 to len of an array
    So, we can use array elements as index to mark it as visited by making it negative
    Traverse an array:
        if arr[abs(ele)-1] > 0:
            arr[abs(ele)-1] = -1*arr[abs(ele)-1]
        else:
            return abs(ele) # first duplicate
    return -1

    TC: O(n)
    SC:O(1)

"""


def get_first_duplicate(array):
    # method 3
    for i, val in enumerate(array):
        if array[abs(val) - 1] > 0:
            array[abs(val) - 1] = -1 * array[abs(val) - 1]
        else:
            return abs(val)
    return -1


if __name__ == '__main__':
    input_array = [2, 1, 2, 4, 5, 3, 2, 1]
    print(get_first_duplicate(input_array))
