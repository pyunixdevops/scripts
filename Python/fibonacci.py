#!/usr/bin/python3

def fib_gen(max1):
    a, b = 0, 1
    for i in range(max1):
        yield(a)
        a, b = b, a + b
print(fib_gen(10))             #<generator object fib at 0x01342480>

print(list(fib_gen(10)))

print(' '.join(str(x) for x in list(fib_gen(10))))

for i in fib_gen(10):
    print(i, end=' ')

print()

def fib_func(max1):
    a, b = 0, 1
    fib_list=[]
    for i in range(max1):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

print(fib_func(10)) 

def fib_func2(max1):
    a, b = 0, 1
    fib_list=[]
    num=0
    while num < max1:
        fib_list.append(a)
        a, b = b, a + b
        num+=1
    return fib_list

print(fib_func2(10)) 

def fib_func3(max1):
    a, b = 0, 1
    fib_list=[]
    num=0
    while a <= max1:
        fib_list.append(a)
        a, b = b, a + b
        num+=1
    return fib_list

print(fib_func3(10)) 
