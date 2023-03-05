def check_power_of_2(val):
    """power of 2 no.s have only a bit set
        so, if we subtract 1 from given 2's power val and take & with val
        results to zero , so we can say it is power of two
    """
    if not val:
        # for val == 0
        return False
    if not val & (val - 1):
        return True
    return False


def check_power_of_k(n, k):
    if not n or not k or n < k:
        return False
    if not ((n >> k) & (k - 1)):
        return True
    return False


if __name__ == '__main__':
    # print(check_power_of_2(2))
    print(check_power_of_k(5, 4))
