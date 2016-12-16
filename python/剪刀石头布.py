#coding=utf-8

import random
while True :
    A=raw_input("请输入:剪刀,石头,布：")
    D ={"剪刀":1,"石头":2,"布":3}
    print '用户：',A,D[A]

    B = random.randint(1,3)
    C ={1:'剪刀',2:"石头",3:"布"}
    print "电脑：",C[B],B


    if D[A]== 1:
            if B== 1:
                print "平局"
            elif B == 2:
                print "你输了"
            elif B == 3:
                print "你赢了"

    if D[A] == 2:
            if B == 1:
                print "你赢了"
            elif B == 2:
                print "平局"
            elif B == 3:
                print "你输了"

    if D[A] == 3:
            if B == 1:
                print "你输了"
            elif B == 2:
                print "你赢了"
            elif B == 3:
                print "平局"
