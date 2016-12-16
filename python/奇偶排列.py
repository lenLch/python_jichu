#!/usr/bin/python
#coding=utf-8
'''
def num(number):
    a = l[i]/2%
    if a=0:
        appendl[]
    if a!=1
        appendl2[]
        return l1,l2
p =l[1,2,5,8,4,7,5,8,4,7,7,7,1,8,2,5]
print p
'''

def fun(l):
    i = 0
    j = len(l)-1

    while i < j:
        while l[i]%2 !=0:
            i += 1
        while l[j]%2 ==0:
            j -= 1

        l[i],l[j] = l[j],l[i]

l = [1,2,3,4,5,6,7,8,9,10]
print "befort:",l

fun(l)
print "after:",l
