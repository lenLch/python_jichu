
def fun(a,b):
    # print a,b
    a += 1
    b += 1
    return a + b,a - b,a * b,a / b

x,y = 3,2
print fun(x,y)
