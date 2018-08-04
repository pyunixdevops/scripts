#!/usr/bin/python3

import math

def is_prime1(num):
    if num> 1:
        if num== 2:
            print('TRUE')
            return True
        if num% 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num) + 1), 2):
            if num% i == 0: 
                return False
        return True
    return False


def is_prime2(num):
    """Finding prime number for a given number"""

    num_sqrt=int(math.sqrt(num))+1
    if num%2==0:
        print("This is not a prime number", num) 
    else:
        for i in range(3, num_sqrt, 2):
            if num % i == 0:
                print("This is NOT a prime number", num, i)
                break
        else:
             print("This is the prime number", num)



def fib_gen(max1):
    a, b = 0, 1
    for i in range(max1):
        yield(a)
        a, b = b, a + b

def fib_func1(max1):
    a, b = 0, 1
    fib_list=[]
    for i in range(max1):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


def fib_func2(max1):
    a, b = 0, 1
    fib_list=[]
    num=0
    while num < max1:
        fib_list.append(a)
        a, b = b, a + b
        num+=1
    return fib_list


def fib_func3(max1):
    a, b = 0, 1
    fib_list=[]
    num=0
    while a <= max1:
        fib_list.append(a)
        a, b = b, a + b
        num+=1
    return fib_list
