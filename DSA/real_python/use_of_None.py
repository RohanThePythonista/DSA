"""
The default value for starter_list evaluates only once at the time the function is defined,
so the code reuses it every time you don’t pass an existing list.

The right way to build this function is to use None as the default value,
then test for it and instantiate a new list as needed:
"""


def bad_function(new_elem, starter_list=[]):
    starter_list.append(new_elem)
    return starter_list


def good_function(new_elem, starter_list=None):
    if starter_list is None:
        starter_list = []
    starter_list.append(new_elem)
    return starter_list


"""
Do use the identity operators is and is not.
Do not use the equality operators == and !=.

The equality operators can be fooled when you’re comparing user-defined objects that override them:
"""


class BrokenComparison:
    def __eq__(self, other):
        return True


b = BrokenComparison()
print(b == None)  # Equality operator   don't do it ---->return True because == override in class
print(b is None)  # Identity operator   do it       ---->return False because None can't be override
