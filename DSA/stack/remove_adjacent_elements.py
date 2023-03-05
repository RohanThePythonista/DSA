"""
Stacks can be used to remove duplicate characters from a string that are stacked next to each other. For example, we take the string aabbccccc and convert it into abc. We can push the first character into a stack and skip if the top of the stack is equal to current character.

You are given a string str. You need to remove the consecutive duplicates.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing string str.

Output Format:
For each testcase, in a new line, print the modified string.

Your Task:
This is a function problem. You need to complete the function removeConsecutiveDuplicates() that takes string as parameter and returns the modified string. The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= |str| <= 103

Examples:
Input:
2
aaaaaabaabccccccc
abbccbcd

Output:
ababc
abcbcd
"""


def removeConsecutiveDuplicates(s):
    stack = list()
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        elif char == stack[-1]:
            continue
    return ''.join(stack)
