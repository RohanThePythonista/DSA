class Parent(object):
    def __init__(self, id1):
        self.id1 = id1
        print("I am called from child:{}".format(id(self.id1)))
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def call_me(self, string):
        self.callback(string)


class Child1(Parent):

    def __init__(self, id1):
        super(Child1, self).__init__(id1)
        # print(self.callback())

    def set_callback(self, callback):
        self.callback = callback


class Child2(Parent):

    def __init__(self, id1):
        super(Child2, self).__init__(id1)
        # print(self.callback())

    def set_callback(self, callback):
        self.callback = callback


def callback1(name):
    print(" I am callback:{}".format(name))


if __name__ == '__main__':
    # p = Parent(None)
    # p.set_callback(callback1)
    c1 = Child1(7)
    c1.set_callback(callback1)
    c1.call_me("c1")
    c2 = Child2(77)
    c2.set_callback(callback1)
    c2.call_me("c2")
