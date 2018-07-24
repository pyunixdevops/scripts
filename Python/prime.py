#!/usr/bin/python3

import math

def prime_no(num):
    """Finding prime number for a given number"""

    start=num
    num_sqrt=int(math.sqrt(num))+1
    if num%2==0 or num%5==0:
        print("This is not a prime number", num) 
    else:
        for i in range(3, num_sqrt, 2):
            if num % i == 0:
                print("This is not a prime number", num, i)
                break
        else:
             print("This is the prime number", num)


prime_no(97)
prime_no(2)
prime_no(9797787)
prime_no(19)
prime_no(17)
prime_no(13)
prime_no(29)
prime_no(37)
