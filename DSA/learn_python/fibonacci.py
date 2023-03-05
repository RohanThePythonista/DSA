import time


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


"""
0 1 1 2 3 5 8
"""
t = time.time()
print(fib(40))
print(time.time() - t)

fib_list = [-1] * 100
fib_list[0] = 0
fib_list[1] = 1


def fib2(n):
    if fib_list[n] != -1:
        return fib_list[n]
    fib_list[n] = fib2(n - 1) + fib2(n - 2)
    return fib_list[n]


t = time.time()
print(fib2(40))
print(time.time() - t)
