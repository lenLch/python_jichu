
a = input()
b = input()
c = input()
# if a > b > c:
#     print a,b,c
# if c > a > b:
#     print c,a,b
# if a > c > b:
#     print a,c,b
# if b > a > c:
#     print b,a,c
# if b > c > a:
#     print b,c,a
# if c > b > a:
#     print c,b,a
if a > b:
    a,b=b,a
if a > c:
    a,c=c,a
if b > c:
    b,c=c,b
print 'a = %d,b = %d,c = %d'%(a,b,c) 
