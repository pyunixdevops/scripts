#!/usr/bin/python3

def outer():
    """This DOCSTR is *** from outer"""
    def inner(msg="HHHIII"):
        """This DOCSTR is --- from inner"""
        print("Print func --- inner()", msg)
        return ("return from inner()", msg)
        
    print("Print outer func ***")
    inner("MY-BYE")
    return inner()

def decor1(dec_msg="My first Decorator"):
    """This is the decorator"""
    print("Print from Decorator", dec_msg)
    return ("return from Decorator", dec_msg)

#print(outer())
#print(decor())
#print(decor("This is an arg to Decorator...."))
print(decor(outer))
