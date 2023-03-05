"""
Given a sorted array. create an array of squares of given array which should be sorted.
-10000 < arr_ele < 10000
e.g. array = [1,2,3] output =[1,4,9]
e.g. array = [-1,-2,-3] output =[1,4,9]
e.g. array = [-3,-2,-1] output =[1,4,9]
e.g. array = [-5,-4,1,2,3] output =[1,4,9,16,25]

Method 1: Naive approach
    Create an squared array
    sort it
    TC: O(nLogn)
    SC:O(1)

Method 2: Better approach
    Use two pointers start and end on input array for traverse and comparison
    Create an squared array of size len(input_array) with default values as zero
    Now traverse array with two pointers
        squared_array_end = len(array) -1
        while start <= end:
            check if arr[start]^2 >= arr[end]^2:
                squared_array[end] = arr[start]^2
                start += 1
            else:
                squared_array[end] = arr[end]^2
                end -= 1
            squared_array_end -= 1
    TC:O(n)
    SC:O(1)
"""


def get_squared_array(array):
    # method 2
    print("input array:{}".format(array))
    n = len(array)
    squared_array = [0 for _ in range(n)]
    squared_end = n - 1
    start = 0
    end = n - 1
    while start <= end:
        start_square = array[start] ** 2
        end_square = array[end] ** 2
        if start_square >= end_square:
            squared_array[squared_end] = start_square
            start += 1
        else:
            squared_array[squared_end] = end_square
            end -= 1
        squared_end -= 1
    return squared_array


if __name__ == '__main__':
    input_array = [-5, -4, 1, 2, 3]
    print("squared_array_sorted_array:{}".format(get_squared_array(input_array)))
