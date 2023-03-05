def count_no_of_set_bits(n):
    # brian karnighan algorithm --> O(no.of set bits)
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count


def countSetBits(n):
    # count all set bits from 1 to N both inclusive
    count = 0
    for i in range(1, n + 1):
        while i > 0:
            i = i & (i - 1)
            count += 1
    return count


if __name__ == '__main__':
    val = 7
    print("no_of_set_bits in {} are:{}".format(val, count_no_of_set_bits(val)))
