#!/usr/bin/python3

import sys
import re

def super_reduced_string(s):
    # Complete this function
    regex=re.compile(r'(\w)(\1)')
    reg=regex.search(s)
    while reg:
        s=s.replace(reg.group(), '')
        reg=regex.search(s)
    #print(s if s else 'Empty String')
    return s if s else 'Empty String'

print("Please input a string:")
s = input().strip()
result = super_reduced_string(s)
print(result)
