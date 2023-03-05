"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


def get_first_and_last_index(nums, target):
    return [get_left_index(nums, target), get_right_index(nums, target)]


def get_left_index(nums, target):
    if not nums:
        return -1
    if nums[0] == target:
        return 0
    left = 0
    right = len(nums)
    while left <= right:
        mid = (left + right) // 2
        # [1,2,3,3,3,3,4,5,9]

        print(left, right, mid)
        if mid > 0 and nums[mid] == target and nums[mid - 1] != target:
            return mid
        elif nums[mid] < target:  # important check to decide which half to go
            left = mid + 1
        else:
            right = mid - 1
    return -1


def get_right_index(nums, target):
    if not nums:
        return -1
    if nums[-1] == target:
        return len(nums) - 1
    left = 0
    right = len(nums)
    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid)
        if mid < len(nums) - 1 and nums[mid + 1] != target and nums[mid] == target:
            return mid
        elif mid < len(nums) and nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# print(get_first_and_last_index([5, 7, 7, 8, 8, 10], 8))
# print(get_first_and_last_index([1, 2, 3], 3))
# [1,2,3,3,3,3,4,5,9]
# 3
print(get_first_and_last_index([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))

"""
# LC solution 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1
"""
