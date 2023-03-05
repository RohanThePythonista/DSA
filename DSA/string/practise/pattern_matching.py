"""
find all matching patterns start indexes in string
e.g. string = 'ABCABCD'
        pat = 'ABCD'
        output:3
At 3rd index in string pat is matched

Naive approach:O((n-m+1)*m)
for i= 0 to n len(string)
    for(j=0 to m len(pat))
        if string[i+j] != pat[j]:
            break
    else:   # j==m else executes when for loop terminate without break statement
        print(i)

Naive approach can work in O(n) time if there are no continuous repeated chars in string and pattern
Idea is to use sliding window and matching technique
    if pattern doesn't match at middle of it then, just jump by len of remaining pat in sting
"""


def match_pattern(string, pat):
    for i in range(len(string)):
        for j in range(len(pat)):
            if string[i + j] != pat[j]:
                break
        else:  # this block executes only when inner for loop exhaust without break in middle
            print(i, end=' ')


def match_distinct_char_pattern(string, pat):
    n = len(string)
    m = len(pat)
    i = 0

    while i <= n-m:
        j = 0
        while j < m:
            if string[i + j] != pat[j]:
                break
            j += 1
        if j == m:
            print(i, end=' ')
            i += 1
        else:
            if j != 0:
                i += j
            else:
                i += 1


if __name__ == '__main__':
    ip_str = 'ABCDABCDABCD'
    pattern = 'ABCD'
    match_distinct_char_pattern(ip_str, pattern)
