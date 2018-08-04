#!/usr/bin/python3.5

import re
s1="abccdefgh123456ABCDEF"
s2="abccdefghABCDEF"
s3="abd"
s4="a\\b\\d"

pt1=re.compile('abc.')
pt2=re.compile('DEF*')
pt3=re.compile('DEFK*')
pt4=re.compile('DEFKM*')
pt5=re.compile('123.')
pt6=re.compile('([a-z]*)([0-9]*)')
pt7=re.compile('([a-z]+)([0-9]+)')
pt8=re.compile('([a-z])([0-9])')
pt9=re.compile('([a-z]*)')
pt9=re.compile('([a-e]*)')
pt9=re.compile('(a.*)')
pt9=re.compile('(a.+)')
pt9=re.compile('(abc+d)')
pt9=re.compile('(abc*d)')
pt9=re.compile('([a-z]*)')
pt9=re.compile('([a-z]+)')
#pt9=re.compile('([a-z].*)')
#pt9=re.compile('([a-z].*)')
#pt9=re.compile('\d+')
#pt9=re.compile('\d')
#pt9=re.compile('\w+')
#pt9=re.compile('\w')

print(pt1, pt2, pt3, sep='..')

print("re.search1", re.search(pt1, s1))
print("re.match1", re.match(pt1, s1))
print("re.search2", re.search(pt2, s1))
print("re.match2", re.match(pt2, s1))
print("re.search3", re.search(pt3, s1))
print("re.search4", re.search(pt4, s1))
print("re.search5", re.search(pt5, s1))
print("re.search6", re.search(pt6, s1))
print("re.search7", re.search(pt7, s1))
print("re.search8", re.search(pt8, s1))
print("re.search9, s2", re.search(pt9, s2))
print("re.search9", re.search(pt9, s1))
print("re.search9", re.search(pt9, s1))
print("re.match9, s3", re.match(pt9, s3))
print("re.search9, s3", re.search(pt9, s3))

m=re.search(pt6, s1)
print(m.groups())
