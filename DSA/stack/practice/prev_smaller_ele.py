def prev_smaller_ele(arr):
    stack = list()
    for val in arr:
        if stack and stack[-1] > val:
            while stack and stack[-1] > val:
                stack.pop()
            if not stack:
                print(-1, end=' ')
            else:
                print(stack[-1], end=' ')
        elif stack and stack[-1] < val:
            print(stack[-1], end=' ')
        else:
            print(-1, end=' ')
        stack.append(val)


if __name__ == '__main__':
    array = [15, 10, 18, 12, 4, 6, 2, 8]
    #     op: -1, -1, 10, 10, -1, 4, -1, 2
    prev_smaller_ele(array)
