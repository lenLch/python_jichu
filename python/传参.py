

def fun(a,b):
    print a,b

def fun1(a,b= 100,c=1000):
    print a,b,c

def fun2(a,*b):
    print a , b

def fun3(a,**b):
    print a,b

def fun4(a,d=100,*b,**c):
    print a,b,c,d
fun(1,2)
fun1(1,2)
fun2(1,2,3,4,5,6)
fun3(1,b=2,c=4)
fun4(1,2,3,4,b=1,c=7)
