def square(data):
    return data * data


square_list = list(map(square, range(10)))
print(square_list)


def sq(x):
    return lambda x: x * x


square_list = [lambda x: x * x for x in range(11, 21, 1)]
print(square_list)
