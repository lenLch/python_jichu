#!/usr/bin/python

d = {}
l = [[5,3,8,6],[4,7,2,9],[3,1,6,4]]

a = max(l[0])
b = max(l[1])
c = max(l[2])

d[a] = [0,l[0].index(a)]
d[b] = [1,l[1].index(b)]
d[c] = [2,l[2].index(c)]

l1 = [a,b,c]

max = max(l1)

print "max = %d "%max,d[max]
