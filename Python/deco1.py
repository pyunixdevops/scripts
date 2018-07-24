#!/usr/bin/python3

def f1(l1):
    return([x for x in l1 if x%2==0])

#Calling function with args and assign the value
f2=f1(range(1,5))
#print(f1())
#f2=f1()
print(f1(range(1,5)))
print(f2)
print("type of f2-{f2}, type of f1-{f1}".format(f1=type(f1),f2=type(f2)))

#Calling function without args and assign the value
f3=f1
print(f3(range(1,5)))
print(f3)
print("type of f3-{f3}, type of f1-{f1}".format(f1=type(f1),f3=type(f3)))
print(f1(range(1,9)))

def f5(a,b):
    while a != b:
       if a > b:
           a-=1
           print(a)
       else:
           b-=1
           print(b)
       return f5(a,b)
    return (a,b)

print(f5(4,9))
