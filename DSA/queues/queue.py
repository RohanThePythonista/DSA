class Deque:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def deque(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    d = Deque()
    d.enqueue("prachi")
    d.enqueue("rohan")
    print(d.deque())
    print(d.deque())
