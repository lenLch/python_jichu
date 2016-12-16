#!/usr/bin/python
#coding=utf-8
class Node(object):  #用 class创建结点 
    def __init__(self,value,next = None):  #创建一个结点，元素域为value，地址域为next
        self.value = value
        self.next = next



class Linklist(object):
    def __init__(self):       #初始化一个链表,创建一个列表
        self.head = None    #创建一个头结点，赋值为none

    def __getitem__(self,key): #魔法方法，当对象使用中括号时，自动调用这个函数,可以直接使用[value]
            if self.is_empty():
                print"linklist is empty"
                return
            else:
                return self.getitem(key) #调用getitem函数，输入[下标]，显示下标位置的值

    def __setitem__(self,key,value):   #魔法方法，当用中括号赋值时，自动调用这个函数
        if key < 0 or key > self.getlength():
            print "The given key is error"
            return
        else:
            self.defete(key)
            return self.insert(key,value) #调用insert函数，直接利用[下标]重新进行赋值

    def initlist(self,data):    #初始化一个链表
        self.head = Node(0)    #把0赋给self.head定义头指针，头标记，标记链表的初始位置，为了找到下个位置
        p = self.head

        for i in data:   #顺次往链表中增加结点
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):    # 链表长度
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next
        return length



    def show(self):   #展示结果，每次都要调用
            p = self.head.next

            while p !=None:
                print p.value,
                p = p.next
            print ""
    def is_empty(self):
        if self.getlength() == 0:    # 判断长度是否为空
            return True
        else:
            return False

    def clear(self): #清空列表
        self.head = None

    def append(self,value):  #在末尾增加结点
        p = self.head
        q = Node(value)
        while p.next != None:
            p = p.next
        p.next = q

    def insert(self,index,value):#在index位置插入value
        if index < 0 or index >self.getlength(): #建立约束条件，防止越界
            print " index is error"
            return

        p = self.head  #创建结点

        i = 0
        while p.next != None and i < index:  #循环在插入位置结束
            p = p.next
            i += 1

        q = Node(value)    #传入value，确定结点值，定义为q
        q.next = p.next   #使两个结点连在一起，线把后面链接在一起，在链接前面，q.next表示为为下一个结点，等于p.next
        p.next = q

    def defete(self,index):  #按位置删除结点，输入下标，删除值
        if index < 0 or index >self.getlength() - 1:
            print " index is error"
            return

        p = self.head

        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1

        if p.next == None:
            print 'index is error'

        else:
            p.next = p.next.next

    def index(self,value):  #输入value，查找结点位置
        if self.is_empty():
            print "Linklist is empty"
            return
        p = self.head.next
        i = 0
        while p != None and not (p.value == value):
            p = p.next
            i += 1

        if p == None:
            return -1
        else:
            return i
    def getitem(self,index):  #输入位置，输出值
            if self.is_empty():
                print "Linklist is empty"
                return
            p = self.head.next
            i = 0
            while p != None and i < index:
                p = p.next
                i += 1

            if p == None:
                return "target is not exist"
            else:
                return p.value
