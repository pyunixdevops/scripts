#!/usr/bin/python

def calDistinctPairs(a, k):
    mset=list(sorted(set(a)))
    count=0
    rcount=0
    mlist1=[]
    for i in mset:
        for j in mset[count+1:]:
            if sorted([i,j]) not in mlist1:
                mlist1.append(sorted([i,j]))
                if i + j == k:
                     print(i,j)
                     rcount+=1
        if a.count(i) >= 2:
            if sorted([i,j]) not in mlist1:
                mlist1.append(sorted([i,j]))
                if i + i == k:
                    print(i,i)
                    rcount+=1

    return rcount


m=[3,4,5,6,7,8,9,2,2,4,5,6,7,8]
l=10
print(calDistinctPairs(m,l))
                

