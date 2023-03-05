"""
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Try to solve it in O(n log k) time and O(n) extra space
"""

from collections import OrderedDict


def top_k_frequent_words(word_list, k):
    word_count = OrderedDict()
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    count_dict = dict()
    for key, value in word_count.items():
        if value in count_dict:
            count_dict[value].append(key)
        else:
            count_dict[value] = [key]
    counts = sorted(count_dict.keys(), reverse=True)
    res = []
    for cnt in counts:
        for w in sorted(count_dict[cnt]):
            res.append(w)
            if len(res) == k:
                return res


if __name__ == '__main__':
    # a = ["aaa", "aa", "a"]
    a = ["i", "love", "leetcode", "i", "love", "coding"]
    # a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    # a = ["i", "love", "leetcode", "i", "love", "coding"]
    print(top_k_frequent_words(a, 3))
