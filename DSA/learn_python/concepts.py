"""
iterator Vs iterable?
-->consider a book
    no. of pages in book can be iterate
        -->is iterable--->lists, dict, tuple, set, array
            -->produces an iterator
    bookmark in book
        -->is iterator
        --->it tells/gives us obj where it is exactly while iterating over iterable
        -->used in generators
        -->it can be any value which produces stream of values
        -->only operation in iterators is next()
iterator = iter(iterable) # or iterable.__iter__()
value = next(iterator)  # or iterator.next() or iterator.__next__()
value = next(iterator)
...




Abstract and customize your iterations!
See how you can use more generators and __iter__ method in your code

what is xrange?--->it is an obj which is iterator

How to approach modifying list while iterating over it?
-->best approach would be to create new list
-->There is problem if we are iterating over list from starting and remove any ele
    -->It will miss next element while it traverse
        --suppose it is at 4th ele and if we delete it
            -->then 5th will come to 4th place
                -->so it is missed in next iteration
-->other hack is to travers list from back and modify it if required
"""


# my_dict = {'name': 'rohan', 'id': 1}
# print(my_dict)
# popped = my_dict.pop('name')
# print(popped)
# print(my_dict)
# popped = my_dict.pop('id')
# print(popped)
# print(my_dict)
# popped = my_dict.pop('age', None)
# print(popped)
# print(my_dict)

class InTest(object):
    def __init__(self, my_list):
        self.test_list = my_list

    def __contains__(self, item):
        # this method makes class as iterable object
        for index, val in enumerate(self.test_list):
            if val == item:
                return True
        return False


# map() returns an iterator object
# map(function, iterable)
pets = ('bird', 'snake', 'dog', 'turtle', 'cat', 'hamster')
uppercased_pets = list(map(str.upper, pets))

# below is list comprehension to replace above map usage
pets = ('bird', 'snake', 'dog', 'turtle', 'cat', 'hamster')
uppercased_pets = [pet.upper() for pet in pets]

# Nested List Comprehensions
#  for readability, it’s not recommended to have more than two levels.
nested_numbers = ((1, 4, 7, 8), (2, 3, 5))
squares = [x * x for numbers in nested_numbers for x in numbers]

# use of walrus in python 3.8+ in list comprehension
# import random
# letters = list('this is to produce a list of letters')
# vowels = [letter.upper() for _ in range(0, 10) if (letter := random.choice(letters)) in list('aeoui')]

# syntax for set comprehension
# {expression for item in iterable}


# syntax for dict comprehension
# {key_expression : value_expression for item in iterable}
if __name__ == '__main__':
    input_list = [i for i in range(1000)]
    test = InTest(input_list)
    print(-1 in test)
