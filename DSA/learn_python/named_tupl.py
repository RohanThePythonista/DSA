from collections import namedtuple

colour = namedtuple('Colour', ['red', 'green', 'blue', 'test'])

c_test = colour(1, 2, 3, 1)
print(c_test.blue)
print(c_test.count(1))
