"""
find_pat_permutations_in_given_string

Naive approach:
    using sliding window:
    slide window in input string one by one
        count chars in window and match with pat count
    This requires O(n-m)*m  m:pat len n:str len

Better approach:TC:O(n) SC:O(1)~O(256)*2
    Using sliding window and pattern matching
    take two count arrays for str and pat
    initially count char in both for len of pat
    then start from len of pat to len of str:
        check if count arrays are same: # const operations of len 256 every time
            then pat found in string
        for next match create new window for str
            just reduce count_str[ord[i-len of pat]] -= 1
            and add count_str[str[i]] += 1
"""


def find_pat_permutations_in_given_string(string, pat):
    if len(pat) > len(string):
        return False
    count_string = [0] * 256
    count_pat = [0] * 256
    for i in range(len(pat)):
        count_pat[ord(pat[i])] += 1
        count_string[ord(string[i])] += 1
    for i in range(len(pat), len(string), 1):
        if are_same(count_string, count_pat):
            return True
        count_string[ord(string[i])] += 1
        count_string[ord(string[i - len(pat)])] -= 1
    return False


def are_same(string_window, pat_window):
    """
    This check if two arrays with same length 256 have same count of chars
    :param string_window: array with counts of char from input string with len of pat string
    :param pat_window: array with counts of char from pattern string
    :return:bool True if counts are same in both arrays else False
    """
    for i in range(256):
        if string_window[i] != pat_window[i]:
            return False
    return True
