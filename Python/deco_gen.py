#!/usr/bin/python3

def f1(l1):
    return([x for x in l1])

def f2(l2):
    return(y for y in l2)

print(f1(range(1,5)))
print(f2(range(1,9)))
gen1=f2(range(1,9))
print(gen1)
print(list(gen1))

for i in gen1:
    print(i)
print(gen1)
print(list(gen1))
