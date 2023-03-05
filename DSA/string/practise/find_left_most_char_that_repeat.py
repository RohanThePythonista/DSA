import sys

"""
Find index of leftmost char that repeats

Naive approach-TC:O(n^2) SC:O(1)
start string travers from left:
    check if curr left index value is repeating
     at its right remaining string by traversing:
     if found repeated then result curr left index
return -1 if no repeated found

better approach:TC:O(n) SC:O(256)
    use count_array of len 256 with default values to -1
    init res = MAX value # to store final result index
    traverse string from start :
        check if value in count_arr at ascii value of curr char as index is == -1:
            store curr index of curr char at this position
        else:
            res = min(res, count_arr[ord(char)])
    return -1 if res is MAX else res
 
    faster approach than above approach is to traverse string from its end:
        so, that res will be updated directly with repeated char index every time
 
"""


def find_left_most_char_that_repeat(string):
    count_array = [-1] * 256
    res = sys.maxsize
    for index, char in enumerate(string):
        if count_array[ord(char)] == -1:
            count_array[ord(char)] = index
        else:
            res = min(res, count_array[ord(char)])
    return -1 if res == sys.maxsize else res


def find_left_most_char_that_repeat_method2(string):
    count_array = [-1] * 256
    res = sys.maxsize
    for index in range(len(string) - 1, -1, -1):
        char = string[index]
        if count_array[ord(char)] == -1:
            count_array[ord(char)] = index
        else:
            count_array[ord(char)] = index
            res = count_array[ord(char)]
    return -1 if res == sys.maxsize else res


def find_left_most_char_that_not_repeat_method(string):
    count_array = [-1] * 256
    res = sys.maxsize
    for index, char in enumerate(string):
        if count_array[ord(char)] == -1:
            count_array[ord(char)] = 1
        else:
            count_array[ord(char)] += 1
    for index, char in enumerate(string):
        if count_array[ord(char)] == 1:
            return index


def find_left_most_char_that_not_repeat_method2(string):
    count_array = [-1] * 256
    res = sys.maxsize
    for index, char in enumerate(string):
        if count_array[ord(char)] == -1:
            count_array[ord(char)] = index  # this is IMP
        else:
            count_array[ord(char)] = -2  # this is marked repeating
    for val in count_array:  # const loop
        if val >= 0:
            res = min(res, val)  # val is index of leftmost non repeated
    return res


if __name__ == '__main__':
    print(find_left_most_char_that_not_repeat_method2('geeksforgeeks'))
