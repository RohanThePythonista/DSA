"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


def swap_case(s):
    my_str = s.split()
    swap_case_list = list()
    for split in my_str:
        swap_case_list.append(get_swap_case(split))
    return ' '.join(swap_case_list)


def get_swap_case(split):
    my_list = list()
    for char in split:
        if char.isnumeric() or char.isalpha() is False:
            my_list.append(char)
        elif char.islower():
            my_list.append(char.upper())
        elif char.isupper():
            my_list.append(char.lower())
    return ''.join(my_list)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
