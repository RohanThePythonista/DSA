# """
# *
# * *
# * * *
# * * * *
# * * * * *
# """
# j = 0
# for i in range(5):
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print("\n")
#     j = 0
# """
# * * * * *
# * * * *
# * * *
# * *
# *
# """
# for i in range(5):
#     for j in range(4, -1, -1):
#         if i <= j:
#             print("*", end=" ")
#
#     print("\n")
# """
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# """
# for i in range(5):
#     for j in range(4, -1, -1):
#         if j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("\n")
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""
# i = 0
# j = 0
# while i < 5:
#     while j < 5:
#         pass

'''
1
121
12321
1234321
123454321
'''

# i = 0
#
# while i < 5:
#     j = 1
#     val = i + 1
#     flag = 0
#
#     while j <= i * 2 + 1:
#         if j <= val:
#             flag += 1
#             print(j, end=" ")
#         else:
#             flag -= 1
#             print(flag, end=" ")
#         j += 1
#     i += 1
#     print('')


# for i in range(1, 5 + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
#     print('')


"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

   Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

"""

"""
size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

one half
----c
--c-b
c-b-a
blow is reflect 
--c-b
----c
"""

my_string = 'abcdefghijklmnopqrstuvwxyz'
