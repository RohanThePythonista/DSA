"""
Find N_bonaci m numbers --.first n-1 ele always zero in series
means next no. is always sum of last n no.s

Naive approach:
    --> print first n-1 zeros and next 1
        then for i = m-n to m(m is excluded)
        --> then running loop for j = i-n to i(i is included)
                calculate next ele in series using last n eles and print

Better approach: O(m) expected
e.g. n = 3, m = 8
0,0,1,1,2,4,7,13

Find distinct elements in every window of size k
e.g. arr = [1,2,1,3,4,3,3] k =4
    o/p = 3, 4, 3, 2 --->in first 4 eles 1,2,3 are distinct in last 4 eles 3 and 4 are only distinct

naive approach : O(n*k)
    --> for every window of size k use hashmap/hashing(can use dict for it)
        --> so it take n*k iterations

Better approach expected:O(n)
"""


def print_m_fibonacci_no(m):
    first = 0
    second = 1
    for i in range(m):
        print(first, end=' ')
        third = first + second
        first = second
        second = third


if __name__ == '__main__':
    print_m_fibonacci_no(6)
