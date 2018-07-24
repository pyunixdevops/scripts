#!/usr/bin/python3

import sys

print(list(sys.argv))
print(str(sys.argv))
print(sys.argv)
print(type(sys.argv))

l1=[int(x) for x in sys.argv[1:]]
count=0
l3=[]
for i in l1:
    n=len(l1)
    res=0
    while res == n:
        print("i from for-1------", i)
        for j in l1:
            if i <= j:
                res+=1
    else:
        print("Its in else")
        l3.append(i)
        l1.remove(i)
l3.extend(l1)
print(l1)
print(l3)



