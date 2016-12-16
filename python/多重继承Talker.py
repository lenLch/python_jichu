#!/url/bin/python
#coding=utf-8


class Speaker(object):
    name = "mao"

class Calculator(Speaker):
    name = "luosifu"
    age = 88

class Talker(Speaker):
    name = "liyong"
    sex = "man"

class TalkCalculator(Calculator,Talker):
    pass

A = TalkCalculator()

print TalkCalculator.mro()   #显示继承顺序

print A.name
print A.sex
print A.age
