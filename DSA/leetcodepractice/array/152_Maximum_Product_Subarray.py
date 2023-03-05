"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

import math


def max_product(a):
    n = len(a)
    if n == 0:
        return 0
    res = -math.inf
    product_from_front = 1
    product_from_back = 1
    for i in range(n):
        product_from_front *= a[i]
        product_from_back *= a[n - 1 - i]
        res = max(res, product_from_front, product_from_back)
        if not product_from_front:
            product_from_front = 1
        if not product_from_back:
            product_from_back = 1
    return res


if __name__ == "__main__":
    # array = [2, 3, -2, 4]
    array = [-2, 3, -4]

    print(max_product(array))
    print(array)
