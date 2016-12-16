#!/ues/bin/python
#coding=utf-8

print "module1..."
class A(object):
    print "module1->calss A"
    def a(self):
        print "module1-->class A-->def a..."

def b():
    print "module1-->def b..."


    print "++++++",__name__# 别调用==module1

print __name__  # 模块没有被调用时  __name__==__main__

if __name__ == "__main__":  #检测 模块 有没有被调用，当模块被调用时 __name__不等于__main__，将不会执行 这个语句
    print "dosomething..."
