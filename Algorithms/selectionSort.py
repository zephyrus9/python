# -*-coding: utf-8 -*-
# Author:

""" 选择排序"""


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