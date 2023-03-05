stack_1 = []
min_stack = []


def get_min():
    global stack_1
    global min_stack
    if stack_1 and min_stack:
        return min_stack[-1]
    return -1


def push(key):
    global stack_1
    global min_stack
    if not stack_1 or key <= stack_1[-1]:
        stack_1.append(key)
        min_stack.append(key)
    else:
        stack_1.append(key)


def pop():
    global stack_1
    global min_stack
    res = -1
    if stack_1 and min_stack and stack_1[-1] == min_stack[-1]:
        min_stack.pop()
    if stack_1:
        res = stack_1[-1]
        stack_1.pop()
    return res


if __name__ == '__main__':
    push(2)
    push(3)
    print(pop())
    print(get_min())
    push(1)
    print(get_min())