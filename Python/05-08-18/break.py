#!/usr/bin/python3

from math import sqrt
import time
l1=[13,21,19,17,29,47,37,59,67,91,97,41,49,53,73,83,103]

def break_continue(l1):
    prime=[]
    noprime=[]
    for i in l1:
        if i%2==0:
            print("Not Prime", i)
            noprime.append(i)
            continue
        for j in range(3, int(sqrt(i))+1, 2):
            if i%j==0:
                print("Not prime", i)
                noprime.append(i)
                break
        else:
            print("Its prime", i)
            prime.append(i)
            continue
    return (prime, noprime)

def break_continue_v2(my_list):
    prime=[]
    noprime=[]
    for i in my_list:
        for j in range(3, int(sqrt(i))+1, 2):
            if i%j==0:
                print("Not prime", i)
                noprime.append(i)
                break
        else:
            print("Its prime", i)
            prime.append(i)
            continue
    return (prime, noprime)

start_time = time.time()
print(break_continue(l1))
end_time = time.time()
print("Total time taken", end_time - start_time)

start_time = time.time()
print(break_continue_v2(l1))
end_time = time.time()
print("Total time taken", end_time - start_time)

