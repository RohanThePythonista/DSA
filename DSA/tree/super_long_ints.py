import ctypes

"""
PyLongObject represents one bignum as defined
by CPython and will map to `_longobject` of
its internals.

Here we have preallocated ob_digit array to hold
at max 100 digits/elements.
"""


class PyLongObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
        ("ob_size", ctypes.c_ulong),
        ("ob_digit", ctypes.c_uint * 100)
    ]


"""
get_digits function returns ob_digits array
representing how a big number is stored
internally as "digits".

The function returns a list of digits starting
from least significant digit to most significant.
The length of the list implies `ob_size`.
"""


def get_digits(bignum):
    obj = PyLongObject.from_address(id(bignum))
    return obj.ob_digit[:obj.ob_size]


if __name__ == '__main__':
    # num = (2 ** 30) ** 2
    num = 10000000
    digits = get_digits(num)
    print(num, digits)
    print(2**60)
