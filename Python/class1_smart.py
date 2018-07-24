SankarR@Skoruz-SankarR:~$ python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
SankarR@Skoruz-SankarR:~$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> str_tuple="My name is", "Sankar"
>>> type(str_tuple)
<class 'tuple'>
>>> int_tuple=1,2,3,43,4
>>> type(int_tuple)
<class 'tuple'>
>>> print(int_tuple)
(1, 2, 3, 43, 4)
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'int_tuple', 'str_tuple']
>>> def f2(x,y):
...     return x+y
... 
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'f2', 'int_tuple', 'str_tuple']
>>> dir(f2)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(int_tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dir(str_tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> l1=[1,2,3,4,4]
>>> tuple(l1)
(1, 2, 3, 4, 4)
>>> dict(l1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> l2=[(1,2),(3,4),(4,5)]
>>> dict(l2)
{1: 2, 3: 4, 4: 5}
>>> list(dict(l2))
[1, 3, 4]
>>> str(list(dict(l2)))
'[1, 3, 4]'
>>> y=lambda x: x*5
>>> y(23)
115
>>> print(y(23))
115
>>> z=lambda a,b: a+90
>>> u=lambda a,b=10: a+90
>>> z(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() missing 1 required positional argument: 'b'
>>> z(3,)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() missing 1 required positional argument: 'b'
>>> z(3,5)
93
>>> u(3)
93
>>> u1=lambda a=12,b: a+90
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
>>> u=lambda a,b=10: a+90
>>> u(b=21,a=2)
92
>>> u(b=21,c=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() got an unexpected keyword argument 'c'
>>> 
>>> u(b=21,2)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>> u(21,2)
111
>>> def f9_tuple(*val):
...     print(type(f9_tuple))
...     print(f9_tuple)
... 
>>> f9_tuple(12,32,32,3,34,43,5,5,6,6)
<class 'function'>
<function f9_tuple at 0x7fa067d39bf8>
>>> def f9_tuple(*val):
...     print(val)
...     print(type(val))
... 
>>> f9_tuple(12,32,32,3,34,43,5,5,6,6)
(12, 32, 32, 3, 34, 43, 5, 5, 6, 6)
<class 'tuple'>
>>> def f9_tuple(*val):
...     return val
... 
>>> k=f9_tuple(12,32,32,3,34,43,5,5,6,6)
>>> k
(12, 32, 32, 3, 34, 43, 5, 5, 6, 6)
>>> for i in k:
...     print(i)
... 
12
32
32
3
34
43
5
5
6
6
>>> def f9_tuple(**val):
...     return val
... 
>>> k=f9_tuple(12,32,32)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f9_tuple() takes 0 positional arguments but 3 were given
>>> k=f9_tuple(x=12,y=32,z=32)
>>> print(k)
{'x': 12, 'z': 32, 'y': 32}
>>> def f9_tuple(*args, **kwargs):
...     return args, kwargs
... 
>>> m=f9_tuple(23,43,82,x=12,y=32,z=32)
>>> m
((23, 43, 82), {'x': 12, 'z': 32, 'y': 32})



>>> l1=[1,2,3,4,4]
>>> tuple(l1)
(1, 2, 3, 4, 4)
>>> dict(l1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> l2=[(1,2),(3,4),(4,5)]
>>> dict(l2)
{1: 2, 3: 4, 4: 5}
>>> list(dict(l2))
[1, 3, 4]
>>> str(list(dict(l2)))
'[1, 3, 4]'
>>> y=lambda x: x*5
>>> y(23)
115
>>> print(y(23))
115
>>> z=lambda a,b: a+90
>>> u=lambda a,b=10: a+90
>>> z(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() missing 1 required positional argument: 'b'
>>> z(3,)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() missing 1 required positional argument: 'b'
>>> z(3,5)
93
>>> u(3)
93
>>> u1=lambda a=12,b: a+90
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
>>> u=lambda a,b=10: a+90
>>> u(b=21,a=2)
92
>>> u(b=21,c=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() got an unexpected keyword argument 'c'
>>> 
>>> u(b=21,2)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>> u(21,2)
111
>>> def f9_tuple(*val):
...     print(type(f9_tuple))
...     print(f9_tuple)
... 
>>> f9_tuple(12,32,32,3,34,43,5,5,6,6)
<class 'function'>
<function f9_tuple at 0x7fa067d39bf8>
>>> def f9_tuple(*val):
...     print(val)
...     print(type(val))
... 
>>> f9_tuple(12,32,32,3,34,43,5,5,6,6)
(12, 32, 32, 3, 34, 43, 5, 5, 6, 6)
<class 'tuple'>
>>> def f9_tuple(*val):
...     return val
... 
>>> k=f9_tuple(12,32,32,3,34,43,5,5,6,6)
>>> k
(12, 32, 32, 3, 34, 43, 5, 5, 6, 6)
>>> for i in k:
...     print(i)
... 
12
32
32
3
34
43
5
5
6
6
>>> def f9_tuple(**val):
...     return val
... 
>>> k=f9_tuple(12,32,32)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f9_tuple() takes 0 positional arguments but 3 were given
>>> k=f9_tuple(x=12,y=32,z=32)
>>> print(k)
{'x': 12, 'z': 32, 'y': 32}
>>> def f9_tuple(*args, **kwargs):
...     return args, kwargs
... 
>>> m=f9_tuple(23,43,82,x=12,y=32,z=32)
>>> m
((23, 43, 82), {'x': 12, 'z': 32, 'y': 32})
>>> p=1,2,3,4
>>> c=1,
>>> type(c)
<class 'tuple'>
>>> type(p)
<class 'tuple'>
>>> d="test",
>>> type(d)
<class 'tuple'>
>>> range(3)
range(0, 3)
>>> def f9_tuple(*args, **kwargs):
...     return [args, kwargs]
... 
>>> m=f9_tuple(23,43,82,x=12,y=32,z=32)
>>> m
[(23, 43, 82), {'x': 12, 'z': 32, 'y': 32}]
>>> m=f9_tuple(x=12,y=32,z=32)
>>> m
[(), {'x': 12, 'z': 32, 'y': 32}]
>>> m=f9_tuple(x=12,12,y=32,z=32)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>> range(1,20)
range(1, 20)
>>> list(range(1,20))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(1,5,2))
[1, 3]
>>> list(range(1,-5,2))
[]
>>> list(range(-5,1,2))
[-5, -3, -1]
>>> list(range(1,-5,-2))
[1, -1, -3]
>>> x=10
>>> y="Python Class"
>>> x*12
120
>>> y*3
'Python ClassPython ClassPython Class'
>>> y + "NOt interzted"
'Python ClassNOt interzted'
>>> x + 90
100
>>> l2=list(range(1,10))
>>> l2*3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #map(func, iterbale)
... 
>>> map(lambda x: x*3, l2)
<map object at 0x7fa067d91be0>
>>> list(map(lambda x: x*3, l2))
[3, 6, 9, 12, 15, 18, 21, 24, 27]
>>> list(filter(lambda x: x%2==0, l2))
[2, 4, 6, 8]
>>> list(map(lambda x: x%2==0, l2))
[False, True, False, True, False, True, False, True, False]
>>> list(filter(lambda x: x*3, l2))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> reduce(lambda x,y: x+y, l2))
  File "<stdin>", line 1
    reduce(lambda x,y: x+y, l2))
                               ^
SyntaxError: invalid syntax
>>> reduce(lambda x,y: x+y, l2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reduce' is not defined
>>> from functools import reduce
>>> reduce(lambda x,y: x+y, l2)
45
>>> reduce(lambda x,y: x-y, l2)
-43
>>> reduce(lambda x,y: x*y, l2)
362880
>>> enumerate(l2)
<enumerate object at 0x7fa067d24ee8>
>>> list(enumerate(l2))
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
>>> list(enumerate(range(1,10,2))
... 
... 
... )
[(0, 1), (1, 3), (2, 5), (3, 7), (4, 9)]
>>> dict(enumerate(range(1,10,2)))
{0: 1, 1: 3, 2: 5, 3: 7, 4: 9}
>>> [x for x in l2]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x for x in l2 if x%2==0]
[2, 4, 6, 8]
>>> [x for x in l2 if x%2==0 x*2 else x*5]
  File "<stdin>", line 1
    [x for x in l2 if x%2==0 x*2 else x*5]
                             ^
SyntaxError: invalid syntax
>>> [x if x%2==0 x*2 else x*5 for x in l2]
  File "<stdin>", line 1
    [x if x%2==0 x*2 else x*5 for x in l2]
                 ^
SyntaxError: invalid syntax
>>> [x for x in l2 else x*5 if x*2==0 x*3]
  File "<stdin>", line 1
    [x for x in l2 else x*5 if x*2==0 x*3]
                      ^
SyntaxError: invalid syntax
>>> [x for x in l2 else x*5 if x*2==0]
  File "<stdin>", line 1
    [x for x in l2 else x*5 if x*2==0]
                      ^
SyntaxError: invalid syntax
>>> [x for x in l2 else x*5 if x*2==0]
KeyboardInterrupt
>>> [x for x in l2]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> {x for x in l2}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> {x:y for x,y in enumerate(l2)}
{0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9}

