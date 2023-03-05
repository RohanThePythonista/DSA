l = [1, 2]
t = (l, l)
print(t)
"""
Tuple is hashable while list is not.
A tuple can only be used as a key in a dictionary if all of its elements are immutable 
Hash functions return the hash value of the object, if it has one.
tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples).
Lists can never be used as dictionary keys, because lists are not immutable.

the membership of a tuple cannot be changed
but mutable elements of a tuple can be changed
"""
l.append(3)
print(t)

"""
What makes you think tuples are faster then lists?  
check and explore like following example
$ python -m timeit "for x in xrange(10000):" " ''.join( ['a','b','c','d','e','f','g'] )" 1000 loops, best of 3: 1.91 msec per loop
 $ python -m timeit "for x in xrange(10000):" " ''.join( ('a','b','c','d','e','f','g') )" 1000 loops, best of 3: 1.17 msec per loop
"""

"""
One thing to keep in mind is to avoid returning a list (or any other mutable) that's part of your state, 

class ThingsKeeper
    def __init__(self):
        self.__things = []

    def things(self):
        return self.__things  #outside objects can now modify your state

    def safer(self):
        return self.__things[:]  #it's copy-on-write, shouldn't hurt performance
"""

"""
https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
When to use tuple
One example would be pairs of page and line number to reference locations in a book, e.g.:
my_location = (42, 11)  # page number, line number

192

If you went for a walk, you could note your coordinates at any instant in an (x,y) tuple.

If you wanted to record your journey, you could append your location every few seconds to a list.

But you couldn't do it the other way around.
"""

"""
the memory address where the list values are stored is not the 
same as the memory address where the list object itself is stored

, you could add new element to both list and tuple with the 
only difference that you will change id of the tuple by adding element
     = (1,2)
b     = [1,2]  

id(a)          # 140230916716520  ---see
id(b)          # 748527696

a   += (3,)    # (1, 2, 3)
b   += [3]     # [1, 2, 3]

id(a)          # 140230916878160 --see
id(b)          # 748527696
"""
print(('a', 'b', 'c').index('c'))
print(['a', 'b', 'c'].index('c'))