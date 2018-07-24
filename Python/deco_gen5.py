#!/usr/bin/python3

def decor_outer(func1):
    """This DOCSTR is *** from decor_outer"""
    def inner(msg="HHHIII"):
        """This DOCSTR is --- from inner"""
        func1(msg)
        func1()
        out_decor=func1()
        print(out_decor)
        print("Print func --- inner()", msg)
        return ("return from inner()", msg)
        
    print("Print decor_outer func ***")
    inner("MY-BYE")
    return inner

@decor_outer
def regular(msg="HI-from regular-regular"):
    """This is the regular"""
    #print("Print from regular", msg)
    return ("return from regular", msg)

print(regular())
