"""
Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""

import math
from typing import List


class Solution:
    """
    The thought follows a simple rule:
    If the sum of a subarray is positive,
        it has possible to make the next value bigger, so we keep do it until it turn to negative.
    If the sum is negative, it has no use to the next element, so we break.
    it is a game of sum, not the elements.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        curr_subarray = max_sum_subarray = nums[0]  # important for base cases when only ele is present
        for num in nums[1:]:
            curr_subarray = max(num, curr_subarray + num)
            max_sum_subarray = max(max_sum_subarray, curr_subarray)
        return max_sum_subarray


# using Kadane's algorithm
def max_sub_array(arr):
    # idea is to keep adding element till curr ele unless its sum so far is greater than curr ele
    # update the sum so far curr ele in place of curr ele's index and then at last return max of array updated
    for i in range(1, len(arr)):
        arr[i] = max(arr[i], arr[i] + arr[i - 1])
    return max(arr)


if __name__ == "__main__":
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(array))
    print(max_sub_array(array))
