#!/usr/bin/python3

def squares(start, stop):
    for i in range(start, stop):
        yield i * i

# Generator is a stateful object. You can use next() to call its values.
# Generator is a subclass of an Iterator. However, an Iterator cannot be a Generator.
generator1 = squares(2,12)

generator2 = (i*i for i in range(1,11))

print(generator1)
print(generator2)

"""
class Squares(object):
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop
    def __iter__(self): return self
    def next(self):
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current

iterator1 = Squares(5, 15)

print(iterator1)

def a_function():
"""
"""
just a function definition with yield in it"""    
    yield

print(type(a_function))

a_generator = a_function()

print(type(a_generator))

import collections, types

print(issubclass(collections.Iterator, collections.Iterable))
print(isinstance(a_generator, collections.Iterator))

Generators:

Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s __iter__() method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the __iter__() and next() [__next__() in Python 3] methods. More information about generators can be found in the documentation for the yield expression.

class Yes(collections.Iterator):
    def __init__(self, stop):
        self.x = 0
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes'
        else:
            # Iterators must raise when done, else considered broken
            raise StopIteration 
    __next__ = next # Python 3 compatibility


def yes(stop):
    for _ in range(stop):
        yield 'yes'


yes_expr = ('yes' for _ in range(stop))

stop = 4

for i, ys in enumerate(zip(Yes(stop), yes(stop), ('yes' for _ in range(stop))):
    print('{0}: {1} == {2} == {3}'.format(i, y1, y2, y3))


"""


def foo():
    print "begin"
    for i in range(3):
        print "before yield", i
        yield i
        print "after yield", i
    print "end"

f = foo()
print(f.next())
print(f.next())
"""

