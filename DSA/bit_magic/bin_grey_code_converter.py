def bin_grey_converter(n):
    q = (n >> 1)
    return n ^ q


def grey_to_bin_converter(n):
    b = 0
    while n > 0:
        b = (b ^ n)
        n = (n >> 1)
    return b


g = bin_grey_converter(7)
b_ = grey_to_bin_converter(g)
print(g, b_)
