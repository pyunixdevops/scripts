#!/usr/bin/python3

l2=[]
def func2(num):
    x=num//2
    y=num%2
    l2.append(y)
    if x >= 1:
        print(x)
        print(y)
        return func2(x)
    return l2
    
print(func2(10))

