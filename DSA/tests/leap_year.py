def check_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


if __name__ == '__main__':
    print(check_leap_year(1900))
