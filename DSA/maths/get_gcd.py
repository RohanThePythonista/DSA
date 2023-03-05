def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def get_gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return get_gcd(b, a % b)


if __name__ == '__main__':
    print(2 % 7)
    print(gcd(12, 3))

    # a= 7 = 1,7
    # b= 2 = 1, 2
    # gcd = 1 i.e. highest common factor greatest common divisor

    # a= 12 = 1,2,3,4,6,12
    # b= 3 = 1,3
    # gcd = 3
