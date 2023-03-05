def max_consecutive_ones(x):
    # e.g. x= 95 (1101111)
    """
    Steps
        1. x & x<<1 --> 1101111 & 1011110 == 1001110
        2. x & x<<1 --> 1001110 & 0011100 == 0001100
        3. x & x<<1 --> 0001100 & 0011000 == 0001000
        4. x & x<<1 --> 0001000 & 0010000 == 0000000
    :param x:
    :return:
    """
    count = 0
    while x > 0:
        x = x & (x << 1)
        count += 1
    return count


if __name__ == '__main__':
    print(max_consecutive_ones(7))
