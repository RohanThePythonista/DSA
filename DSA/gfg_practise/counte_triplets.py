"""
Given an array arr[] of distinct integers of size N and a value sum,
    the task is to find the count of triplets (i, j, k),
    having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

Input: N = 4, sum = 2
arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with
sum less than 2 (-2, 0, 1) and (-2, 0, 3).

"""


class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        counter = 0
        for i in range(n - 1):
            j = i + 1
            k = n - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] < sumo:
                    counter += (k - j)
                    j += 1
                else:
                    k -= 1

        return counter
