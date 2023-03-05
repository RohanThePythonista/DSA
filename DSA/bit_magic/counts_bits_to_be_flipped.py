def count_bits_flip(a, b):
    res = a ^ b
    count = 0
    while res > 0:
        res = res & (res - 1)
        count += 1
    return count


if __name__ == '__main__':
    print(count_bits_flip(10, 20))
