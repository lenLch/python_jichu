#coding=utf-8
def fun(a,b):
     print a,b

fun(1,2)
fun(1,b=2)
fun(b=2,a=1)

l= [5,6]
fun(*l)

d = {"b":1,"a":3}
fun(**d)

def fun1(x,*args,**kwargs):
    print x , args , kwargs
fun1(1,1,5,7,a=7)
