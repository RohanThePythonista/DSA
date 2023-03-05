"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.



Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1


Constraints:

1 <= bad <= n <= 231 - 1
"""

"""
Day1: 12/Oct:
this is related to binary search problem
basically we need to find the first occurrence of the bad version in given versions list 1 to n

here is induction proof:http://www.cs.cornell.edu/courses/cs211/2006sp/Lectures/L06-Induction/binary_search.html
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

"""
class Solution:
    def firstBadVersion(self, n):
        
        start  = 1
        
        while start < n: # important: as it linked to end = mid update
        
            mid = start + (n- start)//2
                                    
            if isBadVersion(mid):
                # go to left half as we have to find first occurrence 
                n = mid # this is related to loop condition    
            else:
                start = mid + 1
        
        return start
"""


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if isBadVersion(1):
            # base case
            return 1

        start = 1

        while start <= n:  # important to making right to mid-1 n = bad -1 here

            bad = start + (n - start) // 2

            if isBadVersion(bad) and bad > 1 and not isBadVersion(bad - 1):
                # found the first occurrence having prev is good version
                return bad

            elif isBadVersion(bad):
                # go to left half  by setting upper bound to middle-1 as we have to find first occurrence
                n = bad - 1

            else:
                start = bad + 1


def isBadVersion(pick: int) -> int:
    global bad_version
    if bad_version == pick:
        return True
    return False


if __name__ == "__main__":
    s = Solution()
    n = int(input())
    bad_version = int(input())
    result = s.firstBadVersion(n)
    assert (bad_version == result)
    print(f"your bad_version {result=} is correct")
