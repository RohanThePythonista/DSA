class Stack:
    def __init__(self, capacity_of_stack):
        self.top = -1
        self.capacity = capacity_of_stack
        self.arr = [0 for i in range(self.capacity)]

    def push(self, key):
        if self.is_overflow():
            print("stack is overflow, push aborted for key {}".format(key))
            return
        self.top += 1
        self.arr[self.top] = key

    def pop(self):
        if self.is_empty():
            print("stack is underflow, pop aborted")
            return
        print("pop:{}".format(self.get_top()))
        self.top -= 1

    def get_top(self):
        if self.top >= 0:
            return self.arr[self.top]

    def is_empty(self):
        return self.top == -1

    def is_overflow(self):
        return self.top == self.capacity - 1

    def print_stack(self):
        if not self.is_empty():
            top = self.top
            print("printing stack")
            while top >= 0:
                print(self.arr[top], end=" ")
                top -= 1
        else:
            print("stack is empty, print is useless")
        print("\n")


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.print_stack()

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.print_stack()
