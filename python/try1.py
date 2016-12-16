#!/usr/bin/python
#coding=utf-8
def div(a,b):
    try:  #   建立一个捕捉，try   捕捉错误
        c = a / b
        print "c:",c
    except(TypeError,ZeroDivisionError):     #不同异常，相同结果处理
        print "zero can not be divsion or num error"
    else:                 #except  不执行时  ，执行 else
        print "else..."
    finally:             #任何时候 都执行
        print "finally..."
        return c
result = div(3,1)

print result
print "test over"
