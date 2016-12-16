
k=1
for i in range(2,100):
    for j in range(2,i):
        k = i% j
        if k == 0:
            break
    if k !=0:
        print "%d"%i,

'''
#!/usr/bin/python
#coding=utf-8

flag = 1
for num in range(2,100):
    for i in range(2,num):
        if num % i == 0:
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        print "%d"%num
'''
