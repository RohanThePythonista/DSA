def is_sparse(n):
    return not n & (n >> 1)


if __name__ == '__main__':
    print(is_sparse(3))  # 11000
    print(bin(10 ** 3))
