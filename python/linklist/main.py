#!/usr/bin/python
#coding=utf-8
from linklist import*

l = Linklist()

l.initlist([1,2,3,4,5])
l.show()

print l.getlength()

l.append(10)
l.show()

l.append(20)
l.show()

l.insert(2,30)
l.show()

l.defete(3)
l.show()

print l.index(30)

print l.getitem(4)

print l[4] #只有定义 __getitem__函数，才可以shiyong

l[4] = 40  # 只有定义__setitem__函数，才可以使用
l.show()
