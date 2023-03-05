"""
check_if_two_strings_are_rotations_of_each_other
 use concat for any string with itself and find other in this modified string
 use sliding window and matching
"""


def check_if_two_strings_are_rotations_of_each_other(string1, string2):
    n1 = len(string1)
    n2 = len(string2)
    if n1 != n2:
        return False
    string1 += string1
    s1 = []
    s2 = []
    for i in range(n1):
        s1.append(string1[i])
        s2.append(string2[i])
    for i in range(n1, (n1 + n2), 1):
        if check_if_match_found(s1, s2) is True:
            return True
        s1.append(string1[i])
        s1.pop(0)
    return False


def check_if_match_found(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


if __name__ == '__main__':
    print(check_if_two_strings_are_rotations_of_each_other('aabb', 'bbaa'))
