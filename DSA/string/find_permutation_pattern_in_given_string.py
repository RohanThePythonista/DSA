"""
find if permutation of given pattern exist in given string text
-->use sliding window technique + any algo to check window string and pattern anagram(use xor approach)

"""


def find_pattern(string, pat):
    """
    this is naive approach
    it takes O((n-m+)*m)
    :param string:
    :param pat:
    :return:
    """
    str_len = len(string)
    pat_len = len(pat)
    start_window = 0
    end_window = pat_len
    for i in range(str_len - pat_len):
        if are_anagrams(string[start_window:end_window], pat):
            print(i)
        start_window += 1
        end_window += 1


def find_pattern_2(string, pat):
    """
    This method works in O(n) time
    Idea is to have count array of pattern and string for given len of pattern which stores frequency of chars of
    pattern char and other string chars
    It iterate over string form 0 to n-m n is len of string and m is len of pat
    Sliding window technique is used to iterate over string
    :param string:
    :param pat:
    :return:
    """
    text_window_count = [0 for _ in range(256)]
    pat_window_count = [0 for _ in range(256)]
    text_len = len(string)
    pat_len = len(pat)
    for i in range(pat_len):
        text_window_count[ord(text[i])] += 1
        pat_window_count[ord(pat[i])] += 1
    for i in range(text_len - pat_len):
        if is_anagrams(text_window_count, pat_window_count):
            return True
        text_window_count[ord(text[i])] -= 1
        text_window_count[ord(text[i + pat_len])] += 1
    return False


def is_anagrams(pat_window_count, text_window_count):
    for i in range(256):
        if pat_window_count[i] != text_window_count[i]:
            return False
    return True


def are_anagrams(str1, str2):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return False
    res = ord(str1[0])
    for i in range(1, n1, 1):
        res ^= ord(str1[i])
    res2 = ord(str2[0])
    for i in range(1, n1, 1):
        res2 ^= ord(str2[i])
    return res ^ res2 == 0


if __name__ == "__main__":
    text = "geeksforgeeks"
    pattern = "egek"  # "geek"
    # find_pattern(text, pattern)
    print(find_pattern_2(text, pattern))
