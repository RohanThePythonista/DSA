class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def deque(self):
        while not self.stack2:
            if not self.stack1:
                return
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return self.stack1 == []

    def size(self):
        return len(self.stack1)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    # print(q.deque())
    # for i in range(-1, -5, -1):
    #     print(i)
