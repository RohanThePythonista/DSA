"""
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. T testcases follow. Each case contains a string S containing characters.

Output:
For each test case, in a new line, output a single line containing the reversed String.

Constraints:
1 <= T <= 100
1 <= |S| <= 2000

Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr
"""


def reverse_word_order_in_string(string):
    word_list = []
    word = ''
    for char in string:
        if char != '.':
            word += char
        else:
            word_list.append(word)
            word = ''
    word_list.append(word)
    word_list = list(reversed(word_list))
    return '.'.join(word_list)


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        input_str = input()
        print(reverse_word_order_in_string(input_str))
