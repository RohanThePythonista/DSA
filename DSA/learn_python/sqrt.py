"""
https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/
"""


def get_sqrt(x, prec):
    low = 1
    high = x
    res = 1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            res = mid
            break
        if mid * mid > x:
            high = mid - 1
        else:
            low = low + 1
            res = mid

    # increment = 0.1
    # for i in range(0, prec):
    #     while res * res <= x:
    #         res += increment
    #
    #         # loop terminates when ans * ans > number
    #     res = res - increment
    #     increment = increment / 10

    return res


if __name__ == '__main__':
    import time

    t = time.time()
    n = pow(2, 50)
    precision = 0
    print("{p:.{prec}f}".format(p=get_sqrt(n, precision), prec=precision))
    print(time.time() - t)
