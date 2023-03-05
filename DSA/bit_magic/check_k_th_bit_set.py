def is_k_th_bit_set(n, k):
    # here left shift operator used to generate no with k_th bit set

    if k and n & (1 << k - 1):
        return True
    return False


if __name__ == '__main__':
    print("is_k_th_bit_set(10, 2):{}".format(is_k_th_bit_set(10, 2)))
