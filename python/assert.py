#!/urs/bin/python
#coding=utf-8

a = input()

try:
    assert a> 5    #异常处理    输入错误时，会弹出异常，交给 except处理
    if a > 5:
        print "a > 5"
    else:
        print "a < 5"
except AssertionError:    #接收assert 弹出的异常信息
    print "No assert error"
