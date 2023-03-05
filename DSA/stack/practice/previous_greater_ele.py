def find_prev_greater_ele(arr):
    stack = []
    for val in arr:
        if stack and stack[-1] > val:
            print(stack[-1], end=' ')
        elif stack and stack[-1] < val:
            while stack and stack[-1] < val:
                stack.pop()
            if not stack:
                print(-1, end=' ')
            else:
                print(stack[-1], end=' ')
        else:
            print(-1, end=' ')
        stack.append(val)


if __name__ == '__main__':
    array = [15, 10, 18, 12, 4, 6, 2, 8]
    # o/p = -1, 15, -1, 18, 12,12,6,12
    find_prev_greater_ele(array)
