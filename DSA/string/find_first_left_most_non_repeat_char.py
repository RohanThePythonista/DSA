"""
find first non-repeat char's leftmost index in given string text

Method 1: Naive approach
    Using two loops
    for each character i
        seen = False
        check for j =i+1 to n
            if str[i] == str[j]:
                    seen = True
                    break
            if seen is False:
                return str[i]  # first non-repeat char
    TC: O(n^2)

Method 2:Better approach
    Use constant space array of len 256 with default values -1
    Use character's ascii value as index for marking visited char
    traverse input string for each letter:
        ascii_index = ord(letter)
        if arr[ascii_index]== -1:
            mark this value with current traverse index i
        elif arr[ascii_index] != -1:
            it suggests it was visited once
            make it now -2 -->indicates visited second or more than second time
            arr[ascii_index] = -2
    Now traverse array to find non-repeated
        check if ele != -2 and ele != -1:
            return ele
    TC:O(n)
    SC:O(1)-->constant space depending on input char set
"""


def left_most_index_non_repeat(string):
    first_index = [-1 for _ in range(256)]
    for i, letter in enumerate(string):
        ascii_index = ord(letter)
        if first_index[ascii_index] == -1:
            first_index[ascii_index] = i
        elif first_index[ascii_index] != -1:
            first_index[ascii_index] = -2
    for i, val in enumerate(first_index):
        if val != -2 and val != -1:
            return val
    return - 1


if __name__ == '__main__':
    text = "abcdjjkabcd"
    print(left_most_index_non_repeat(text))
