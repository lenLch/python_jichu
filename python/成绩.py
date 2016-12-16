#!/usr/bin/python

a = input()
if a<0 or a >100:
    print "xxx"
elif 60<= a <= 100:
    if a >=90:
        print "A"
    elif 80<= a :
        print "B"
    elif 70<= a :
        print "C"
    elif 60<= a :
        print "D"
else:
    print "E"
