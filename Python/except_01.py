#!/usr/bin/python3

try:
    fh2=open('my_except.txt', 'r')
    with open('/root/test1.txt', 'w') as fh3:
        fh3.append('This is my new line')
    #except:
    #    print("Unable to open /root/test1.txt for writing")
    #finally:
    #    print("Successfully opened the file")
#except IOError:
except IndexError:
   print("Failed to open file, non existent - my_except.txt")
finally:
   print("Executed finally, finally :-)")
    
