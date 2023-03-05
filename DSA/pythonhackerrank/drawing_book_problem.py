#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p == 1 or p == n:
        # first or last page
        return 0
    mid_page = n // 2
    if mid_page > p:
        # flip pages from start of book and get count
        return p // 2
    elif mid_page <= p:
        # flip pages from end of book and get count
        flips = (n - p) // 2
        if flips < 1 and n % 2 == 1:
            # odd no pages and last page on right side
            return 0
        elif flips < 1 and n % 2 == 0:
            # even no pages and last page on left side
            return 1
        return flips

# one line solution with basic maths
# min(flips_till_asked_page_from_left_to_right, total_flips_from_left_to_right_minus_flips_till_asked_page_from_left_to_right)
# min(p//2, n//2 - p//2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
