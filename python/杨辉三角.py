#!/urs/bin/python
#coding=utf-8
d = [1]
for i in range(11):
    i += 1
    d[i] = d[i] + d[i+1]
    print d
