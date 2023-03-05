import math


def digit_sum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    print(sum)
    range_type = range(8)
    print(range_type, type(range_type))


def quadraticRoots(a, b, c):
    val = b * b - 4 * a * c
    print(val)
    common = None
    try:
        common = math.sqrt(val)

        d1 = -b * b + common / 2
        d2 = -b * b - common / 2
        print(d1, d2, sep=" ")
    except ValueError as error:
        # if common < 0:
        #     print("Imaginary")
        #     return
        print(error)


if __name__ == '__main__':
    quadraticRoots(1, 3, 4)
# if __name__ == '__main__':
#     digit_sum(225)
