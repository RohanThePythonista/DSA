n = 10
r_shift = n >> 1
print(r_shift)
l_shift = n << 1
print(l_shift)

k = 3
if 7 & (1 << k-1):
    print("set")
