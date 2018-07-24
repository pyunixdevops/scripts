#!/usr/bin/python3

def f1(l1):
    return([x for x in l1])

def f2(l2):
    return(y for y in l2)

f3=f1(range(1,5))
print(f1(range(1,5)))
print(f3)

f4=f1

print(f4(range(1,5)))
