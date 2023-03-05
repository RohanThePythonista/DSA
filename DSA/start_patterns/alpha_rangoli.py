import string

alpha = [chr(ascii_val) for ascii_val in range(97, 97 + 26)]
# print(alpha)
n = 3
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(s, s[::-1], s[1:])
    L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print(L)
# print('\n'.join(L[:0:-1] + L))

# i_p = "rohan"
# o_p = i_p.center(20, '*')
# print(o_p, len(o_p))
