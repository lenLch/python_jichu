#!/usr/bin/python
#!coding=utf-8

class Node(object):
    def __init__(self,value,prior= None):
        self.value = value
        self.prior = prior
        self.next = next

class Linklist(object):
    def __init__(self):
        self.head = None

    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            node.prior = p
            p = p.next
        p.next = self.head
        self.head.prior = p

    def show(self):
        p = self.head.next
        while p !=self.head:
            print p.value,
            p = p.next
        print ""

    def getlength(self):    # 链表长度
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:    # 判断长度是否为空
            return True
        else:
            return False

    def insert(self,index,value):
        if index < 0 or index > self.getlength():
            print "index is error"
            return
        p = self.head
        i = 0
        while p.next != self.head and i < index:
            p = p.next
            i += 1
        q = Node(value)

        q.next = p.next
        p.next.prior = q
        p.next = q
        q.prior = p

    def delete(self,index):
        if index < 0 or index > self.getlength():
            print "index is error"
            return
        p = self.head
        i = 0
        while p.next != self.head:
            p = p.next
            i += 1
        p.next = p.next.next
        p.next.next.prior = p
