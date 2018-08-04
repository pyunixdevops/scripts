#!/usr/bin/python3

def countDistPairs(list1, val1):
    """Pass a list and the resulting pair of value"""
    mset=list(sorted(set(list1)))
    count=0
    rcount=0
    mlist1=[]
    for i in mset:
        for j in mset[count+1:]:
            if sorted([i,j]) not in mlist1:
                mlist1.append(sorted([i,j]))
                if i + j == val1:
                     print(i,j)
                     rcount+=1
        if list1.count(i) >= 2:
            if sorted([i,j]) not in mlist1:
                mlist1.append(sorted([i,j]))
                if i + i == val1:
                    print(i,i)
                    rcount+=1

    return rcount

