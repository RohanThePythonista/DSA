class TwoStackInArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top1 = -1
        self.top2 = capacity
        self.stack = [-1] * capacity

    def push1(self, key):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack[self.top1] = key
        else:
            print(f"stack1 is full")

    def pop1(self):
        if self.top1 == -1:
            print(f"stack1 is empty")
            return -1
        res = self.stack[self.top1]
        self.top1 -= 1
        return res

    def push2(self, key):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stack[self.top2] = key
        else:
            print(f"stack2 is full")

    def pop2(self):
        if self.top2 == self.capacity:
            print(f"stack2 is empty")
            return -1
        res = self.stack[self.top2]
        self.top2 += 1
        return res


if __name__ == '__main__':
    two_stack = TwoStackInArray(10)
    for i in range(6):
        two_stack.push1(i)
    for i in range(10, 20):
        two_stack.push2(i)
    for i in range(10):
        print(two_stack.pop1())
    for i in range(10):
        print(two_stack.pop2())
