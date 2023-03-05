class A(object):
    def __init__(self):
        print("I am from A")

    def print_data(self, value):
        print("value:{}".format(value))
        print("I am from A")


class B(A):
    def __init__(self):
        super().__init__()
        print("I am from B")

    def print_data(self, value):
        print("value:{}".format(value))
        print("I am from B")


class C(A):
    def __init__(self):
        super().__init__()
        print("I am from C")

    def print_data(self, value):
        print("value:{}".format(value))
        print("I am from C")


class D(B, C):
    """
    A
   / ⇘
  B ⇐ C
   ⇘ /
    D
    """

    def __init__(self):
        super().__init__()
        print("I am from D")


class A2(object):
    def __init__(self):
        print("I am from A2")


class B2(A2):
    def __init__(self):
        print("I am from B2")
        super().__init__()


class C2(A2):
    def __init__(self):
        print("I am from C2")
        super().__init__()


class D2(B2, C2):
    """
    A
   / ⇖
  B ⇒ C
   ⇖ /
    D

    """

    def __init__(self):
        print("I am from D2")
        super().__init__()


import logging


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Settingto %r' % (key, value))
        super().__setitem__(key, value)


if __name__ == '__main__':
    d = D()
    print(D.__mro__)
    d.print_data("roney")
    # d2 = D2()
    # print(D2.__mro__)
