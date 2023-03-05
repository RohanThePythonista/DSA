n = 5


def recursive_fact(val):
    if val == 0:
        return 1
    return val * recursive_fact(val - 1)


def tail_recursive_fact(val, fact=1):
    if val == 0:
        return fact
    return tail_recursive_fact(val-1, fact*val)


def iterative_fact(val):
    fact = 1
    for i in range(val):
        fact = fact * (i + 1)
    return fact


if __name__ == "__main__":
    print(recursive_fact(n))
    print(iterative_fact(n))
    print(tail_recursive_fact(n))
