def naive_next_greater_element(array):
    """
    TC-O(n^2)
    Idea is to use two loops
        One is from i =0 to n
            other is from j =i+1 to n
                keep checking for greater ele for curr element
                if found
                    print(array[j], end=" ")
                    break
            else:
                print(-1, end=" ") ---> this reaches only if inner loop exhaust
    :param array:
    :return:
    """
    n = len(array)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if array[j] > array[i]:
                print(array[j], end=" ")
                break
            j += 1
        else:
            print(-1, end=" ")
        i += 1


def better_next_greater_element(array):
    stack = list()
    """
    # a = [13, 7, 6, 12]
    # output : -1, 12, 12, -1
    Idea is to use stack for checking next greater ele for curr    
    keep adding ele to stack:
        but if curr ele > than stacks top ele
            then keep pop up ele from stack until it gets empty or new top becomes grater than curr ele
                print("ele:{}--->its next greater{}".format(stack[-1], array[i]))
    last check if stack is not empty
        print -1 as there next greater ele
    :param array: 
    :return: 
    """
    i = 1
    n = len(array)
    stack.append(array[0])
    while i < n:
        while len(stack) != 0 and array[i] > stack[-1]:
            print("ele:{}--->its next greater{}".format(stack[-1], array[i]))
            stack.pop()
        stack.append(array[i])
        i += 1
    while len(stack) != 0:
        print("ele:{}--->its next greater{}".format(stack[-1], -1))
        stack.pop()


if __name__ == '__main__':
    a = [13, 7, 6, 12]
    # output : -1, 12, 12, -1
    # naive_next_greater_element(a)
    better_next_greater_element(a)
