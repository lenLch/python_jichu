
#coding=utf-8

import random



while True:
    a = input()
    b = random.randint(1,10)
    print "b = %d"%b
    if a == b:
        print "你猜对了"
        break
    elif a < b:
        print "你猜小了"
    elif a > b:
        print "你猜大了"
