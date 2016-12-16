#!/urs/bin/python
#coding=utf-8

import module1
import module2 as m

s = "main-->s..."

module1.b()
print m.s

m1 = module1.A()
m2 = m._C()

reload(module1)#重新载入模块，在显示一边

m1.a()
m2.c()

print module1.__name__  #调用模块时，__name__等于被调用模块的名称
