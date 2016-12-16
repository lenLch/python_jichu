#!/usr/bin/python
#coding=utf-8
l = [9,8,5,6,3,4,6,1]

def bubble_sort(l):        #冒泡排序
    for i in range(len(l)):
        for j in range(len(l) - i -1):
            if l[j] > l[j + 1]:
                l[j],l[j + 1] = l[j + 1],l[j]
    print(l)


def selection_sort(l):    #选择排序
    for i in range(len(l)):
        min = i
        for j in range(i + 1,len(l)):
            if l[min]>l[j]:
                min = j
        if i!= min:
            l[i],l[min] = l[min],l[i]
    print(l)

def insertion_sort(l):       #插入排序
    for i in range(1,len(l)):
        s = l[i]
        j = i
        while j > 0 and l[j - 1] > s:
            l[j] = l[j - 1]
            j -= 1
        l[j] = s
    print(l)

def sub_sort(array,low,high):    #快速排序
    key = array[low]
    while low < high:
        while low < high and array[high] >=key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] < key:
            low +=1
        array[high] = array[low]
    array[low] = key
    return low
def quick_sort(array,low,high):
    if low < high:
        key = sub_sort(array,low,high)
        quick_sort(array,low,key - 1)
        quick_sort(array,key + 1,high)


def BinSearch(array,t):    #查找，列表必须按顺序排列
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high)//2
        if array[mid] < t:
            low = mid +1
        elif array[mid] > t:
            high = mid + 1
        else:
            return array[mid]
    reyurn -1


bubble_sort(l)

selection_sort(l)

insertion_sort(l)

quick_sort(l,0,len(l) - 1)
print(l)

print(BinSearch(bubble_sort(l),6))
