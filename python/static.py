#!/urs/bin/python
#coding=utf-8
class TestStaticMethod(object):
    #age = 10
    # @staticmethod   #装饰器
    def foo():
        # print TestStaticMethod.age #用类名调用
        print'calling static method foo()'
    foo = staticmethod(foo) #静态 不传参  静态方法可用类名直接调用

class TestClassMethod(object):
    # @classmethod    #装饰器
    def foo(cls):
        print " calling class method foo"
        print "class",cls.__name__#使用类的属性
    foo = classmethod(foo)


A = TestStaticMethod()
A.foo()

B = TestClassMethod()
B.foo()

TestStaticMethod.foo()
TestClassMethod.foo()
