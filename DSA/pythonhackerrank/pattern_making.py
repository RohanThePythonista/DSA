"""
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""


def print_rangoli(size):
    n = size
    alphabets = list(map(chr, range(97, 97 + 26)))
    pattern = alphabets[n - 1::-1] + alphabets[1:n]
    pattern_width = len('-'.join(pattern))
    for i in range(1, n):
        # upper part logic
        # pattern of left + right
        print('-'.join(alphabets[n - 1:n - i:-1] + alphabets[n - i:n]).center(pattern_width, '-'))
    for i in range(n, 0, -1):
        print('-'.join(alphabets[n - 1:n - i:-1] + alphabets[n - i:n]).center(pattern_width, '-'))

    # your code goes here


if __name__ == '__main__':
    n = int(input())
