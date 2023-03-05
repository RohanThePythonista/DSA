def generate_power_set(string):
    n = len(string)
    i, j = 0, 0
    count = 1 << n
    while i < count:
        j = 0
        while j < n:
            if (i & (1 << j)) > 0:
                print(string[j], end="")
            j += 1
        print("\n")
        i += 1


if __name__ == '__main__':
    generate_power_set("abc")
    x = 12
    print((x << 1) + x + (x >> 1))
    # x = 42 / 3
