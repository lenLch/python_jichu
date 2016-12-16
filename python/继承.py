#!/urs/bin/python
#coding=utf-8
class carclass(object):
    shuxing = '四轮 方向 发动机 排气筒'
    def __init__(self,name):
        self.name = name
        print name
    def fun(self):
        print '我是汽车'
class busclass(carclass):
    shuxing1 = '32坐'
    def fun(self):
        print '我是bus'
class paocarclass(carclass):
    name = "paocar"
    shuxing1 = "2坐 4个排气"
    def fun(self):
        print '我是car'
class suvclass(carclass):
    name = "suv"
    shuxing1 = '4坐  4个排气  越野车'
    def fun(self):
        print '我是SUV'
class sonclass(suvclass):
    name = 'suv'
    shuxing1 = "12刚"
    def fun(self):
        print '我是SUV'
bus = busclass("bus")
print bus.shuxing,bus.shuxing1
bus.fun()
paocar = paocarclass("paocar")
print paocar.shuxing,paocar.shuxing1
paocar.fun()
suv = sonclass("suv")
print suv.shuxing,suv.shuxing1,suv.fun()
# suv.fun()
