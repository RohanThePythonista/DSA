a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
print(a * b)


def recursive_multiplication(val_1, val_2):
    if val_1 < val_2:
        recursive_multiplication(val_2, val_1)
    if val_2 <= 0 or val_1 <= 0:
        return 0
    return val_1 + recursive_multiplication(val_1, val_2 - 1)


print(recursive_multiplication(4, 4))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(31, 2))
