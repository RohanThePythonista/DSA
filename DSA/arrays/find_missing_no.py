"""
Given two array
    e.g.     arr_1 = [1, 2, 3, 4, 5, 6, 7]
            arr_2 = [3, 7, 2, 1, 4, 6]
    Find a missing element second array

Method 1:
    Using sum of elements of two arrays
    missing_element = sum_of_elements_of_first_array - sum_of_elements_of_second_array
    TC: O(n)

Method 2:
    Using XOR operation on all elements of both array
    result = 0
    for num in array_1 + array_2:
        result = result XOR num
    finally result would be the missing ele from second array

Method 3:
    Using aux dict as look up table
        add all ele from second array to dict
    and then travers first array:
        check if ele is not present in dict
            then it is missing ele from second array
"""


def find_missing_number_using_sum(arr, arr2):
    """
    This approach may be problematic in case if arrays are two long
        or elements are very small
    """
    complete_sum = 0
    for val in arr:
        complete_sum += val
    missing_sum = 0
    for val in arr2:
        missing_sum += val
    return complete_sum - missing_sum


def finding_missing_using_xor(arr1, arr2):
    """
        XOR of two same no. is zero
    """
    result = 0
    for num in arr1 + arr2:
        result ^= num
    return result


def find_missing_number_using_aux_dict_look_up(arr1, arr2):
    look_up_dict = {}
    for val in arr2:
        look_up_dict[val] = val
    for val in arr1:
        if val not in look_up_dict:
            return val


if __name__ == '__main__':
    arr_1 = [1, 2, 3, 4, 5, 6, 7]
    arr_2 = [3, 7, 2, 1, 4, 6]
    print(find_missing_number_using_sum(arr_1, arr_2))
    print(finding_missing_using_xor(arr_1, arr_2))
    print(find_missing_number_using_aux_dict_look_up(arr_1, arr_2))
