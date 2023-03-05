"""
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
"""
if __name__ == '__main__':
    s = input()
    string_validator = {"any_alphanumeric": False, "any_alphabetical": False,
                        "any_digits": False,
                        "any_lower_case": False, "any_uppercase": False}
    for char in s:
        if ord(char) in range(65, 65 + 25):
            string_validator['any_uppercase'] = True
            string_validator['any_alphanumeric'] = True
            string_validator['any_alphabetical'] = True
        if ord(char) in range(97, 97 + 25):
            string_validator['any_lower_case'] = True
            string_validator['any_alphanumeric'] = True
            string_validator['any_alphabetical'] = True
        if ord(char) in range(48, 58):
            string_validator['any_digits'] = True
            string_validator['any_alphanumeric'] = True
    print(string_validator['any_alphanumeric'])
    print(string_validator['any_alphabetical'])
    print(string_validator['any_digits'])
    print(string_validator['any_lower_case'])
    print(string_validator['any_uppercase'])
#     # In the first line, print True if  has any alphanumeric characters.      Otherwise, print False.
#     # In the second line, print True if  has any alphabetical                characters. Otherwise, print False.
#     # In the third line, print True if  has any digits. Otherwise, print     False.
#     # In the fourth line, print True if  has any lowercase characters.       Otherwise, print False.
#     # In the fifth line, print True if  has any uppercase characters.        Otherwise, print False.

#     if s.isalnum():
#         print(True)
#     else:
#         print(False)

#     if s.isalnum() and not s.isdigit():
#         print(True)
#     else:
#         print(False)

#     if s.isdigit() or (not s.isalpha() and not s.isdigit()):
#         print(True)
#     else:
#         print(False)

#     if (not s.isupper() and not s.islower()) and not s.isdigit() and not s.isspace():
#         # mixedcase
#         print(True)
#     elif s.islower():
#         print(True)
#     else:
#         print(False)

#     if (not s.isupper() and not s.islower()) and not s.isdigit() and not s.isspace():
#         # mixedcase
#         print(True)
#     elif s.isupper():
#         print(True)
#     else:
#         print(False)
