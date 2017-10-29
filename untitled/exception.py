import sys
entry=int(input("enter the number for compliment"))
try:
    print("entry is:",entry)
    r=1/int(entry)
    print ("reciprocal of",entry,"is",r)
except:
    print("oops",sys.exc_info(),"occured")
    print("next entry")
