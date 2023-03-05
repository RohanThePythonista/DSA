def naive_previous_greater(array):
    """
    TC -O(n^2) --->worst case
    Idea is to keep checking for nearby left ele of curr ele for its previous element
    Use two loops:
        one if for curr i = 0 to n
            previous_greater = -1
            other for i-1 to 0
                if we found previous greater ele of curr
                    update previous greater
                    break
            print(previous_greater)
    :param array:
    :return:
    """
    i = 0
    n = len(array)
    while i < n:
        j = i - 1
        previous_greater = -1
        while j >= 0:
            if array[j] > array[i]:
                previous_greater = array[j]
                break
            j -= 1
        print(previous_greater, end=" ")
        i += 1


def better_previous_greater_element(array):
    """
        TC- O(n) ---->actual total operations 2n -->n push -->n pulls in worst case(reverse sorted array input)
        input
        arr = [15, 10, 18, 12, 4, 6, 2, 8]
        output = -1 15 -1 18 12 12 6 12
        i = 1
        stack.append(arr[0])
        print(-1, end=" ") ---> for first ele there is no previous ele exists
        here idea is to use stack to maintain previous greater
            while i < len(arr):
                but when curr ele is greater than stack top element
                    then keep pop elements unless stack empty or top is greater than curr
                if stack is empty
                    -->it means for curr ele > than its all previous elements
                    print(-1)
                else
                    print(stack[-1]) ---> previous greater for curr element
                add curr ele to stack
                    stack.append(array[i])
                i += 1
    """
    stack = list()
    stack.append(array[0])
    n = len(array)
    i = 1
    stack.append(arr[0])
    print(-1, end=" ")
    while i < n:
        while len(stack) != 0 and array[i] > stack[-1]:
            stack.pop()
        if len(stack) == 0:
            print(-1, end=" ")
        # elif array[i] < stack[-1]:
        else:
            print(stack[-1], end=" ")
        stack.append(array[i])
        i += 1


if __name__ == '__main__':
    arr = [15, 10, 18, 12, 4, 6, 2, 8]
    # arr = [18, 10, 20, 19, 17, 12, 21]
    """
    output = -1 15 -1 18 12 12 6 12 
    """
    # naive_previous_greater(arr)
    better_previous_greater_element(arr)
