#!/usr/bin/python3

def outer(func1):
    """This DOCSTR is *** from outer"""
    def inner(msg="HHHIII"):
        """This DOCSTR is --- from inner"""
        func1(msg)
        func1()
        out_decor=func1()
        print(out_decor)
        print("Print func --- inner()", msg)
        return ("return from inner()", msg)
        
    print("Print outer func ***")
    #inner("MY-BYE")
    return inner

@outer
def decor1(msg="HI-from Deco-Deco"):
    """This is the decorator"""
    #print("Print from Decorator", msg)
    return ("return from Decorator", msg)

print(decor1())
