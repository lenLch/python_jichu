#!/urs/bin/python
#coding=utf-8
while True:
    A= raw_input("请输入：年-月-日：")
    l= A.split("-")
    yearflag=0
    monflag=0
    result=0
    dic1 = {1:31,2:29,3:31,4:30,5:30,6:31,7:31,8:31,9:30,10:31,11:30,12:31}
    dic2 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    year = int(l[0])
    mon = int(l[1])
    date = int(l[2])
    if year<0 or mon<0 or mon>12 or date<0 or date>31:
        print "兄弟傻吧"
        continue

    if year%400==0 or year%4==0 and year%100!=0:
        yearflag=1
    if mon in [1,3,5,7,8,10,12]:
        pass
    elif mon == 2:
        monflag=2
    else:
        monflag=1
    if monflag==1 and date>30:
        print "这个月只有30天"
        continue
    if monflag==2 and date>29:
        print "闰年二月多少天"
        continue
    if yearflag==0 and monflag==2 and date>28:
        print "平年二月多少天"
        continue
    for i in range(1,mon):
        if yearflag==1:
            result+=dic[i]
        if yearflag==0:
            result+=dic2[i]
    result+=date
    print "%s是%d年的第%d天"%(A,year,result)
    break
