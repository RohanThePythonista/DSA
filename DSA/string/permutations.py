"""
SIMPLE RECURSIVE PYTHON SOLUTION- 0.02s
Approach- permutation [a,b,c,...] = [a + permutation[b,c,...], b + permutation[a,c,..], ...]
"""


def permutation(s):
    if len(s) == 1:
        return [s]
    permutation_list = []
    for a in s:
        remaining = [x for x in s if x != a]
        z = permutation(remaining)
        for t in z:
            permutation_list.append([a] + t)
    return permutation_list


if __name__ == '__main__':
    t = int(input())
    for y in range(t):
        s = str(input())
        l = permutation(s)
        l.sort()
        print(l)
        for i in l:
            for j in i:
                print(j, end="")
            print(end=" ")
        print()
