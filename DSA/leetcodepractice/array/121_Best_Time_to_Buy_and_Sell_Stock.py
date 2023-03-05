"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""
import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        my_min = math.inf
        max_profit = 0
        for price in prices:
            if price < my_min:
                my_min = price
            elif price - my_min > max_profit:
                max_profit = price - my_min
        return max_profit


"""
better solution 

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
The logic to solve this problem is same as "max subarray problem"
using Kadane's Algorithm. Since no body has mentioned this so far,
I thought it's a good thing for everybody to know.

All the straight forward solution should work,
but if the interviewer twists the question slightly by giving
the difference array of prices, Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.

Here, the logic is to calculate the difference
(maxCur += prices[i] - prices[i-1]) of the original array,
and find a contiguous subarray giving maximum profit.
If the difference falls below 0, reset it to zero.

def maxProfit(prices):
    maxCur = 0
    maxSoFar = 0
    for i in range(1, len(prices):
        maxCur = max(0, maxCur += prices[i] - prices[i-1])
        maxSoFar = max(maxCur, maxSoFar)
    return maxSoFar

"""
