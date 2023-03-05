def fun(n):
    if n < 1:
        return
    else:
        print(n, end=" ")
        fun(n - 1)
        print(n, end=" ")


def tail_recursion(val, k=1):
    if val < 1:
        return
    print(k, end=" ")
    return tail_recursion(val - 1, k + 1)


def cumulative_sum(n):
    if n == 0:
        return 0
    return n + cumulative_sum(n - 1)


def sum_of_digits(n):
    if n <= 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def traditional_sum_of_digits(n):
    s = 0
    while n > 0:
        t = n % 10
        s = t + s  # for revers s = t + s*10
        n = n // 10
    print(s)


def word_split(string, list_of_words, out=None):
    if out is None:
        out = []
    for word in list_of_words:
        if string.startswith(word):
            out.append(word)
            word_split(string[len(word):], list_of_words, out)
    return out


def reverse_string(string):
    if len(string) == 1:
        return string
    print(string)
    return reverse_string(string[1:]) + string[0]


def string_permutation(string):
    pass


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

"""
0, 1, 1, 2, 3
"""
if __name__ == '__main__':
    print(fib(10))
    print(fib_iter(10))
