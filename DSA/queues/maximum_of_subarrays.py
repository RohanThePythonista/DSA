"""
Given an array A and an integer K.
Find the maximum for each and every contiguous subarray of size K.

Input Format:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case contains a single integer N denoting the size of array and the size of subarray K.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output Format:
For each testcase, in a new line, print the maximum for every subarray of size k.

Your Task:
This is a function problem.
You only need to complete the function max_of_subarrays that prints the answer.
The newline is automatically appended by the driver code.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ K ≤ N
0 ≤ A[i] <= 107

Example:
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90

Explanation:
Testcase 1: Starting from first subarray of size k = 3,
 we have 3 as maximum.
 Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6.
"""

from collections import deque

"""
https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
"""


def print_max_in_sub_arrays(arr, n, k):
    """
    O(n) solution using dequeue
    :param arr:
    :param n:
    :param k:
    :return:
    """
    qi = deque()
    # process first k elements
    for i in range(k):
        while qi and arr[qi[-1]] <= arr[i]:
            qi.pop()
        qi.append(i)
    for i in range(k, n):
        # print previous window largest element whose index at front in queue
        print(str(arr[qi[0]]) + " ", end=" ")
        # remove indexes from queue which are out of current window
        while qi and qi[0] <= i - k:
            qi.popleft()
        # remove all queue elements(indexes) which are less than current element in array
        while qi and arr[qi[-1]] <= arr[i]:
            qi.pop()
        qi.append(i)
    print(str(arr[qi[0]]))  # last window largest


def print_largest(arr, n, k):
    """
    O(n*k) using built max on python iterable
    :param arr:
    :param n:
    :param k:
    :return:
    """
    for i in range(n):
        print(max(arr[i:i + k]), end=" ")
        if i == n - k:
            break


if __name__ == "__main__":
    a = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    print_max_in_sub_arrays(a, len(a), k)
    print_largest(a, len(a), k)
