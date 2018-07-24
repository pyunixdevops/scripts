#!/usr/bin/python3

import sys

l1=[int(x) for x in sys.argv[1:]]
#print(l1)
count=0
l3=[]
for i in l1:
    res=0
    print(l1)
    for j in l1[count:]:
        if i <= j:
            res+=1
            if res == len(l1):
                l3.append(i)
                l1.remove(i)
                print("From if", l1)
                count+=1
        else:
            l1.remove(i)
            l1.append(i)
            print("From else", l1)

print(l1)
print(l3)



