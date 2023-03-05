def merger(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < b[j]:
            print(a[i], sep=' ')
            i += 1
        else:
            print(b[j], sep=' ')
            j += 1
    while i < n:
        print(a[i], sep=' ')
        i += 1
    while j < m:
        print(b[j], sep=' ')
        j += 1


if __name__ == '__main__':
    from template import template

    arrA = template.get_sequence_list(5)
    arrB = [20, 30, 30, 50]
    merger(arrA, arrB)
