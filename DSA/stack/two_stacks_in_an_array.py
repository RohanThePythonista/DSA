class TwoStackArray:
    """
    This implementation uses stack size efficiently
    Idea is to start two stacks tops from most left and most right side
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * self.capacity
        self.top_1 = -1
        self.top_2 = self.capacity

    def push1(self, data):
        if not self.is_overflow1():
            self.top_1 += 1
            self.stack[self.top_1] = data

    def pop1(self):
        if not self.is_empty1():
            res = self.stack[self.top_1]
            self.top_1 -= 1
            return res

    def size1(self):
        return self.top_1 + 1

    def is_empty1(self):
        if self.top_1 == -1:
            print("stack 1 is empty")
        return self.top_1 == -1

    def top1(self):
        if not self.is_empty1():
            return self.stack[self.top_1]

    def is_overflow1(self):
        if self.top_1 + 1 == self.top_2:
            print("stack 1 is full or stack 2 reached just before stack 1 top")
        return self.top_1 + 1 == self.top_2

    def print1(self):
        if not self.is_empty1():
            print("stack1")
            for i in range(self.top_1 + 1):
                print(self.stack[i], end=' ')
            print('')

    def push2(self, data):
        if not self.is_overflow2():
            self.top_2 -= 1
            self.stack[self.top_2] = data

    def pop2(self):
        if not self.is_empty2():
            res = self.stack[self.top_2]
            self.top_2 += 1
            return res

    def size2(self):
        return self.capacity - self.top_2

    def is_empty2(self):
        if self.top_2 == self.capacity:
            print("stack 2 is empty")
        return self.top_2 == self.capacity

    def top2(self):
        if not self.is_empty2():
            return self.stack[self.top_2]

    def is_overflow2(self):
        if self.top_2 - 1 == self.top_1:
            print("stack 2 is full or stack 1 reached just before stack 2 top")
        return self.top_2 - 1 == self.top_1

    def print2(self):
        if not self.is_empty2():
            print("stack2:")
            for i in range(self.capacity - 1, self.top_2 - 1, -1):
                print(self.stack[i], end=' ')
            print('\n')


if __name__ == '__main__':
    n = int(input())
    two_stack = TwoStackArray(n)
    for i in range(n >> 1):
        two_stack.push1(i)
    for i in range(n >> 1):
        two_stack.push2(i + 5)
    for i in range(10):
        # print("pop1:{}".format(two_stack.pop1()))
        # print("pop2:{}".format(two_stack.pop2()))
        two_stack.push1(i)
        two_stack.push2(i)
    two_stack.print1()
    two_stack.print2()
