#!/usr/bin/python3

import random

def insert_sorted(elem,list):
       if list == []:
           return [elem]
       elif elem < list[0]:
           return [elem] + list
       else:
           return [list[0]] + insert_sorted(elem, list[1:])

def gensort(list):
    sorted_list = []
    for item in list:
        sorted_list = insert_sorted(item, sorted_list)
    return sorted_list

print(gensort([99,3,81,4,5,6,9,1,1,2]))
