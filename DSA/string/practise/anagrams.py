"""
find if given two string are anagrams of each other
anagrams: An anagram is a word or phrase formed by rearranging
        the letters of a different word or phrase,
        typically using all the original letters exactly once.

modify input strings with replacing white spaces and making single word strings
early check case is: check if len of string if not equal then return False

naive approach:TC:O(n^2) SC:O(1)
    using two loops
    for each_char in string1:
        count1 each_char occurrence in string1 :
        count2 each_char occurrence in string2 :
        if count1 != count2 at any point:
        return False
    return True

better approaches
method1:TC:O(n + 256)~ O(n) SC:O(256)-const~O(1)
    Using count array of len 256 with default values 0

    traverse first string:
        store count of each char in count_array using char's ascii value as index in count array
    traverse second string:
        reduce count of each char in count_array using char's ascii value as index in count array

    traverse const len count array:
        if any value in count array is not zero then
            return False
    of all values are 0 in count array then it means strings are anagrams

method2:TC:O(n) SC:O(1)
    using xor operations on ascii values of strings:
    if strings are anagrams then xor result should be zero at the end

    xor of same value is zero.
"""


def check_if_two_strings_are_anagrams(string1, string2):
    # string1 = string1.replace(' ', '')
    # string2 = string2.replace(' ', '')
    string1 = ''.join(string1.split(' '))
    string2 = ''.join(string2.split(' '))
    print(string2, string1)
    if len(string1) != len(string2):
        return False
    count_occurrence = [0] * 256
    for char in string1:
        count_occurrence[ord(char)] += 1
    for char in string2:
        count_occurrence[ord(char)] -= 1
    for count in count_occurrence:
        if count != 0:
            return False
    return True


if __name__ == '__main__':
    print(check_if_two_strings_are_anagrams('rohanprachi', 'rohan prachi'))
