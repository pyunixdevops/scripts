#!/usr/bin/python3

def squares(start, stop):
    for i in range(start, stop):
        yield i * i

# Generator is a stateful object. You can use next() to call its values.
# Generator is a subclass of an Iterator. However, an Iterator cannot be a Generator.
generator1 = squares(2,12)

generator2 = (i*i for i in range(1,11))

print(generator1)
print(generator2)

for i in generator1:
    print(i)
print(next(generator1))
for i in generator1:
    print("HI")
    print(i)
