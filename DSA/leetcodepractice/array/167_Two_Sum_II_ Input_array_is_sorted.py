"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_map = dict()
        for index, value in enumerate(nums):
            if target - value in value_index_map:
                return [value_index_map[target - value] + 1, index + 1]
            value_index_map[value] = index


"""
# two-pointer
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1
 
# dictionary           
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i
 
# binary search        
def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1
"""

# go through solution discussion there
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solution/
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            mid = left + (right-left)//2
            lr_sum = numbers[left] + numbers[right]
            if lr_sum == target:
                return [left+1, right+1]
            elif lr_sum < target:
                left = mid if numbers[mid] + numbers[right] < target else left+1
            else:
                right = mid if numbers[mid] + numbers[right] > target else right -1
"""

if __name__ == "__main__":
    s = Solution()
    input_array = list(map(int, input().split()))
    t = int(input())
    print(s.twoSum(input_array, t))
    """
    i/p
    2 7 11 15
    9
    o/p
    [0, 1]
    
    [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1]
    11
    """
