def get_first_set_bit_pos(n):
    count = 0
    if not n:
        return
    while True:
        if n & (1 << count):
            break
        count += 1
    print(count + 1)


import math

n = 1
print(math.floor(math.log((n ^ n - 1), 2) + 1))  # xor of n and n-1 and take floor of (log base 2 + 1)
# print(2 ^ 2 - 1)  # precedence of arithmetic operator > bitwise operator
if __name__ == '__main__':
    get_first_set_bit_pos(9)
    pass
