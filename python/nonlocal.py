def fun1():
    a = 3
    def fun2():
        nonlocal a
        a +=1
        return a
f = fun1()
print (f)
