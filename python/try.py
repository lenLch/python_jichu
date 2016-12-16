#!/usr/bin/python
#coding=utf-8
def div(a,b):
    try:  #   建立一个捕捉，try   捕捉错误
        c = a / b
        print "c:",c
        return c
    except ZeroDivisionError:  # 遇见错误，返回错误，
        print"zero can not be divsion"
    except TypeError:           # 不同异常的处理
        print "Plass input the right num"
    except:
        pass
    # except(TypeError,ZeroDivisionError):     #不同异常，相同结果处理
        print "zero can not be divsion or num error"

result = div(3,0)

print result
print "test over"
