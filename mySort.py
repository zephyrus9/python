# -*-coding: utf-8 -*-
# Author: 
import math

"""冒泡排序"""
def bubble_Sort(alist):
    for pass_num in range(len(alist)-1, 0, -1):
        for i in range(pass_num):
            if alist[i] > alist[i +1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# test
alist = [2,3,2,33,24,54,23,112,31]
bubble_Sort(alist)
print("冒泡排序：")
print(alist)


"""改善之后的冒泡排序：短路冒泡排序"""
def shortBubbleSort(alist):
    exchanges = True
    pass_num = len(alist) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        pass_num = pass_num - 1
alist2 = [2,3,2,33,24,54,23,112,31]
shortBubbleSort(alist2)
print("短冒泡排序：")
print(alist2)