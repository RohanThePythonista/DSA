import math

n = 1234


def count_digits_iterative(val):
    count = 0
    while val > 0:
        """ int division should be performed for correct result"""
        val //= 10
        count = count + 1
    print("count:{}".format(count))


def count_digits_recursive(val):
    if val <= 0:
        return 0
    return 1+count_digits_recursive(val//10)


def count_digits_by_formula():
    no_of_digits = math.floor(math.log(n, 10)) + 1
    print(no_of_digits)


if __name__ == '__main__':
    count_digits_by_formula()
    value = n
    count_digits_iterative(value)
    print(count_digits_recursive(value))
