#!/usr/bin/python3

import sys

l1=list(sys.argv[1:])
print(type(l1))
l2=list(l1)
print(l2)
count=1
l3=[]
for i in l1:
    l2=list(l1[count:])
    res=1
    for j in l2:
        if int(i) < int(j):
            res+=1
            if res = len(l2):
                l3.append(int(i))
            print("From first while")
            print(i)
            l3.append(int(i))
            res+=1
        else:
            print("From while else")
            l3.append(int(j))
            print(j)
    count+=1

print(l3)



