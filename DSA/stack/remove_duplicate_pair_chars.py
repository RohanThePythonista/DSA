"""
You are given a string str. You need to remove the pair of duplicates.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing string str.

Output Format:
For each testcase, in a new line, print the modified string. If the final string is empty, then print "Empty String".

Your Task:
This is a function problem. You only need to complete the function removePair() that takes string as parameter and returns the modified string.

Constraints:
1 <= T <= 100
1 <= |str| <= 103

Examples:
Input:
2
aaabbaaccd
aaaa
Output:
ad
Empty String

Explanation:
Testcase1: Remove (aa)abbaaccd =>abbaaccd
Remove a(bb)aaccd => aaaccd
Remove (aa)accd => accd
Remove a(cc)d => ad

"""


def remove_pair(input_string):
    stack = list()
    for char in input_string:
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    if not stack:
        return 'Empty String'
    return ''.join(stack)


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        string = input()
        print(remove_pair(string))
