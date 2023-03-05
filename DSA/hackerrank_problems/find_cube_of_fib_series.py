cube = lambda x: x * x * x


def fibonacci(n):
    fib_series_list = list()
    a, b = 0, 1
    for i in range(n):
        fib_series_list.append(a)
        a, b = b, a + b
    return fib_series_list

"""
1
22
333
4444
55555
"""
for i in range(1, 6, 1):
    print((pow(10, i) // 9) * i)

"""
1
121
12321
1234321
123454321
"""
for i in range(1, 6, 1):
    print(pow(pow(10, i) // 9, 2))

if __name__ == '__main__':
    print(list(map(cube, fibonacci(5))))
