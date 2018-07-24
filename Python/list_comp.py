#!/usr/bin/python3

print([int(i)**2 for i in '121asdad334345345' if i.isdigit() if int(i)%2==0 ])
print([int(i)**2 if int(i)%2==0 else int(i)**3 for i in '121as34' if i.isdigit()])

print([int(i)**2 if int(i)%2==0 else int(i)**3 for i in 'as121a345' if i.isnumeric()])
print([int(i)**2 if int(i)%2==0 else None for i in 'as121a345' if i.isnumeric()])
print([int(i)**2 for i in 'as121a345' if i.isnumeric() if int(i)%2==0])
print([int(i)**2 for i in [1,2,3,'a','b','c'] if str(i).isdigit() if int(i)%2==0 ])

l1=[1,2,3,1]
if l1.remove(1) == None: print("Successs"); x=10 ; y=[1,3,4] ; print([ m**3 for m in y])
if l1.append(1) == None: print("Successs"); x=10 ; y=[2,5,9] ; print([ m**3 for m in y])
