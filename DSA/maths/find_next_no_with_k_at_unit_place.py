def find_next_no_with_k_at_unit_place(n, k):
    given_unit_place_no = n % 10
    if given_unit_place_no == k:
        return n + 10
    if given_unit_place_no < k:
        return n + (k - given_unit_place_no)
    if given_unit_place_no > k and given_unit_place_no <= 53:
        return n + (k + given_unit_place_no)


if __name__ == '__main__':
    print(find_next_no_with_k_at_unit_place(33, 1))
