#!/urs/bin/python
#coding=utf-8

class ShortInputError(Exception):
    def __init__(self,length,least):
        super(ShortInputError,self). __init__(self)
        self.length = length
        self.least = least


try:
    s = raw_input('') 
