def print_dec_oct_HEXA_bin_of_all_n(n):
    for i in range(1, n+1, 1):
        print("{} {:o} {:X} {:b}".format(i, i, i, i))

if __name__ == '__main__':
    print_dec_oct_HEXA_bin_of_all_n(17)