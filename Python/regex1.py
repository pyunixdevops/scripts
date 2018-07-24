#!/usr/bin/python

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'\W+')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))
