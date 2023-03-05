"""
i/p: [15, 13, 12, 14, 16, 8, 6, 4, 10, 30]
o/p: 1,1,1,3,5,1,1,1,4,10

i/p: [10, 20, 30, 40]
o/p: 1,2,3,4

i/p: [40, 30, 20, 10]
o/p: 1,1,1,1

so, for given input list of stocks
    find span of each stock in list
        span will be count of no. of instances to its left including current ele which are smaller to it

Method 1: Naive approach --> TC: O(n^2) SC: O(1)
    Using two loops
        traverse inner loop to left of current ele until eles are less than curr ele
            and keep counting span if eles are less than current ele

Method 2: Using stack
"""


def calculate_span_of_stocks(arr):
    stack = list()
    stack.append(0)
    i = 1
    while i < len(arr):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if not stack:
            curr_span = i + 1
        else:
            curr_span = i - stack[-1]
        print(curr_span, end=' ')
        stack.append(i)
        i += 1


if __name__ == '__main__':
    array = [15, 13, 12, 14, 16, 8, 6, 4, 10, 30]
    calculate_span_of_stocks(array)
