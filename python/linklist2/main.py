#!/usr/bin/python

from linklist import *

l = Linklist()

l.initlist([1,2,3,4,5])
l.show()

l.getlength()
l.show()

l.is_empty()
l.show()

l.insert(3,10)
l.show()

l.delete(2)
l.show()
