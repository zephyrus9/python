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


# -*-coding: utf-8 -*-
# Author:

""" 选择排序 """
# 时间复杂度与冒泡一样都是O(n^2)，但是交换的次数减少很多，所以会更快的执行；

def selection_sort(alist):
    for fill_slot in range(len(alist) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if alist[location] > alist[pos_of_max]:
                pos_of_max = location

        # sort
        temp = alist[fill_slot]
        alist[fill_slot] = alist[pos_of_max]
        alist[pos_of_max] = temp
    return alist

alist3 = [2,3,2,33,24,54,23,112,31]
selection_sort(alist3)
print("选择排序：")
print(alist3)


""" 插入排序 """


def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue

alist4 = [2,3,2,33,24,54,23,112,31]
insertionSort(alist4)
print("插入排序： ")
print(alist4)


" 归并排序 "
def merge_sort(a_list):
    # splitting the list
    print("Spitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            j += 1
            k += 1

    print("Merging", a_list)

alist5 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist5)
print(alist5)