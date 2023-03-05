def find_next_greater_ele(arr):
    stack = []
    res = []
    for i in range(-1, -len(arr) - 1, -1):
        if stack and stack[-1] < arr[i]:
            while stack and stack[-1] < arr[i]:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
        elif stack and stack[-1] > arr[i]:
            res.append(stack[-1])
        else:
            res.append(-1)
        stack.append(arr[i])
    print(res)


if __name__ == '__main__':
    array = [15, 10, 18, 12, 4, 6, 2, 8]
    # o/p = 18, 18, -1, -1, 6,8,8,-1
    find_next_greater_ele(array)
