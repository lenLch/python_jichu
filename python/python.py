#!/usr/bin/python
import math
a = input("a:")
b = input("b:")
c = input("c:")
d=b**2-4*a*c<0
if d<0:
    print"00"
    exit()
    s= math.sqrt(d)
    x1=(-b+s)/2
    x2=(-b-s)/2
    print "x1:%.2f,x2:%.2f"%(x1,x2)
