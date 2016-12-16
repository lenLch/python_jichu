#!/urs/bin/python
#coding=utf-8

class test(object):
    def __del__(self):
        print "drl...."

    def __enter__(self):
        print "enter"

    def __exit__(self,type,value,traceback):# 当产生错误时，为后面的参数传参
        print "exit...."
        print type
        print value
        print traceback

    def do_something(self):
        return 1/0

with test() as Thing: #用来创建对象，引用之后  创建的对象自动销毁
    print "doing something"
    Thing.do_something()

print "over"
