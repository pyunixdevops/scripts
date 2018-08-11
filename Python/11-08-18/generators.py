#!/usr/bin/python3.5

def fib1(max):
    a, b = 0, 1
    while a < max:
        yield a
        if a > 2:
            break
        a=a+1
        a, b = b, a + b

print(list(fib1(10)))

def fib2(max):
    numbers = []
    a, b = 0, 1
    while a < max:
        numbers.append(a)
        a, b = b, a + b
    return numbers

print(fib2(10))
