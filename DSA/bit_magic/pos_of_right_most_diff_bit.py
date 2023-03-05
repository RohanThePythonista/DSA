def get_pos_of_right_most_different_bits(m, n):
    diff = 0
    while True:
        if (m & (1 << diff)) == (n & (1 << diff)):
            diff += 1
        else:
            break
    return diff + 1


import math

m, n = 52, 4
print(int(math.log((m ^ n) & -(m ^ n), 2) + 1))
# print(log2((m ^ n) & -(m ^ n)) + 1)

if __name__ == '__main__':
    pass
    # print(get_pos_of_right_most_different_bits(52, 4))
