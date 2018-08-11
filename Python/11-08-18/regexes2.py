#!/usr/bin/python3.5

import re
import os
s1="abccdefgh123456ABCDEF"
file_names=re.compile(r"^a.*\.html$")
pyth_file=re.compile(r"^[a-f].*\.py$")
pwd=os.getcwd()
print(pwd)
files=os.listdir(pwd)
print(files)
#list1=re.search(pyth_file, os.listdir(os.getcwd()))
#print(list1)
for file1 in files:
    if re.match(pyth_file, str(file1)):
        print("==------Its a python file", file1)
    else:
        print("Its not a .py extension", file1)
pt1=re.compile('abc.')
