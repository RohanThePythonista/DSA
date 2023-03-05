"""
find first repeat char's leftmost index in given string text
Using array of size of 256 to mark visited char using its ascii value as index in array
Create an array of len 256 with -1 as initial values
Traverse string:
    check its ascii value as index and check if that index in array -1:
        mark it with traverse index i
    check if ascii value as index in array is not -1
        return this first repeated index stored in array at curr char's ascii index
TC: O(n)
SC:O(1)-->256 constant len
"""


def left_most_index(string):
    first_index = [-1 for _ in range(256)]
    for i, letter in enumerate(string):
        ascii_index = ord(letter)
        if first_index[ascii_index] == -1:
            first_index[ascii_index] = i
        elif first_index[ascii_index] != -1:
            return first_index[ascii_index]
    return None


if __name__ == '__main__':
    text = "abcdabcd"
    print(left_most_index(text))
