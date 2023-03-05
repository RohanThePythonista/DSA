class Generator:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > 9:
            raise StopIteration
        return self.count


if __name__ == '__main__':
    for val in Generator():
        print(val)
