"""
input array
    5 8 1 2 10 5 8
outputs
next greater
    8 10 2 10 -1 8 -1
previous greater
    -1 -1 8 8 -1 10 10
next smaller
    1 1 -1 -1 5 -1 -1
prev smaller
    -1 5 -1 1 2 2 5
"""


def next_greater(array):
    """
    Using stack
    if curr ele is greater than top of stack
        pop until top has greater value than curr
        for every pop ele -->next greater is curr element
    at last after array traversal
        if stack has values
            those don't have any next greater element
    :param array:
    :return:
    """
    stack = list()
    print('next greater elements:')
    for curr_ele in array:
        while len(stack) != 0 and stack[-1] < curr_ele:
            print("{} ->{}".format(stack.pop(), curr_ele))
        stack.append(curr_ele)
    while stack:
        print("{} ->{}".format(stack.pop(), -1))


def previous_greater(array):
    """
    Using stack
        top maintained is always greater till prev of curr element traversing
        pop when curr ele is greater than top
        if stack empty then
            print -1 as previous greater of curr ele
        else
            print top as previous greater of curr ele
        push curr ele to stack
    :param array:
    :return:
    """
    stack = list()
    print('previous greater elements:')
    stack.append(array[0])
    print(-1, end=' ')
    i = 1
    n = len(array)
    while i < n:
        while len(stack) != 0 and array[i] > stack[-1]:
            stack.pop()
        if not stack:
            print(-1, end=' ')
        else:
            print(stack[-1], end=' ')
        stack.append(array[i])
        i += 1


def previous_smaller(array):
    """
    Using stack
    Idea is to keep top as smaller till prev of curr ele
    If curr ele is smaller than top ....pop until top is smaller or it becomes empty
    :param array:
    :return:
    """
    stack = list()
    print('previous smaller elements:')
    stack.append(array[0])
    print(-1, end=" ")
    i = 1
    n = len(array)
    while i < n:
        while stack and stack[-1] > array[i]:
            stack.pop()
        if not stack:
            print(-1, end=" ")
        else:
            print(stack[-1], end=" ")
        stack.append(array[i])
        i += 1


def next_smaller(array):
    """
    Using stack:
    1.create empty stack
    2.start traversing array
        -loop:check if stack is not empty and top is greater than curr ele:
            print curr ele as next smaller of pop element
        push curr ele to stack
    3. check if stack is not empty
        loop:pop all ele and print there next smaller as -1
    Idea is to pop all elements from stack if curr ele is less than top until top becomes
    small or stack becomes empty
    for every pop ele -->next smaller is curr element
    after whole traversal of input array
    if anything is left in stack then they don't have any next smaller
    :param array:
    :return:
    """
    print('next smaller elements:')
    stack = list()
    for val in array:
        while stack and stack[-1] > val:
            print("{}-->{}".format(stack.pop(), val))
        stack.append(val)
    while stack:
        print("{}-->{}".format(stack.pop(), -1))


if __name__ == '__main__':
    a = [5, 8, 1, 2, 10, 5, 8]
    # next_greater(a)
    # previous_greater(a)
    # previous_smaller(a)
    next_smaller(a)
