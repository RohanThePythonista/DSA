"""
Sample Input:
2
4
1 2 3 2
1 2
7
86 39 90 67 84 66 62
42 12

Sample Output:
1
-1
"""


def minDist(arr, n, x, y):
    ptr_x = 2 * n
    ptr_y = 2 * n
    min_dist = n
    for index, val in enumerate(arr):
        if val == x:
            ptr_x = index
            min_dist = min(min_dist, abs(ptr_x - ptr_y))
        if val == y:
            ptr_y = index
            min_dist = min(min_dist, abs(ptr_y - ptr_x))
    return -1 if min_dist == n else min_dist


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x, y = list(map(int, input().strip().split()))
        print(minDist(arr, n, x, y))

# } Driver Code Ends
