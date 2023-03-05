"""
round() function in Python
Difficulty Level : Basic
Last Updated : 26 May, 2021
Python provides an inbuilt function round() which rounds off to the given number of digits and returns the floating-point number, if no number of digits is provided for round off, it rounds off the number to the nearest integer.


Syntax:

round(number, number of digits)
round() parameters:

..1) number - number to be rounded
..2) number of digits (Optional) - number of digits
     up to which the given number is to be rounded.
If the second parameter is missing, then the round() function returns:

if only an integer is given, las 15, then it will round off to 15.
if a decimal number is given, then it will round off to the ceil integer after that if the decimal value has >=5, and it will round off to the floor integer if the decimal is <5.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    print(round(meal_cost+ (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100)))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
