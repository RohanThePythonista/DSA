#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    bin_n = bin(n)
    counter = 0
    stack = []
    for bit in str(bin_n):
        if bit == '1':
            stack.append(bit)
        else:
            counter = max(len(stack), counter)
            stack = []
    counter = max(len(stack), counter)
    print(counter)
