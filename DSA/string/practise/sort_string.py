"""
Sort given string from A-Z and a-z, string may contain duplicates char also, string will be single word only

Approach:
    Use ascii values from 0to255(256 values list)
    create arr of len 256 with initial values as zeros
    traverse input string
        increment count at index in array using curr char's ord(ascii)value
    then create result
        use indexes from arr where values are not zero
    finally return join string using this res list
"""


def string_sort_algo(input_string):
    index_array = [0] * 256
    for char in input_string:
        index_array[ord(char)] += 1
    res_list = list(
        map(lambda x: chr(x), [index for index, val in enumerate(index_array) if val != 0 for _ in range(val)]))
    res = ''.join(res_list)
    return res


if __name__ == '__main__':
    print(string_sort_algo('dccaAab'))
