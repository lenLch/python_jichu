#!/usr/bin/python
#coding=utf-8

import traceback # 引用模块   显示错误信息  和 错误位置

def div(a,b):
    try:  #   建立一个捕捉，try   捕捉错误
        return a / b
    except(TypeError,ZeroDivisionError) as e:     # 
        print "zero can not be divsion or num error"
        print e
    else:                 #except  不执行时  ，执行 else
        print "else..."
    finally:             #任何时候 都执行
        print "finally..."
result = div(3,0)

print result
print "test over"
