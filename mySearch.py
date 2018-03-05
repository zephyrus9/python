# -*-coding: utf-8 -*-
# Author: 
import math


"""无序的顺序搜索"""
def sequenceSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            return True
        else:
            pos = pos + 1

    return found

testlist = [2,3,4,5,6,7,8,9,7,61,23,234,54]
print(sequenceSearch(testlist, 52))

""" 有序的顺序搜索"""
def orderedsequenceSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            return True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

testlist2 = [1,2,3,4,55,77]
print(orderedsequenceSearch(testlist2, 5))


""" 二分法搜索"""
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == item:
            found = True
        else:
            if item > alist[middle]:
                first = middle + 1
            else:
                last = middle - 1
    return found

testlist3 = [1,2,3,4,6,7,9,11,14,23,25,33]
print(binarySearch(testlist, 13))
print(binarySearch(testlist3, 14))


""" 用递归实现二分搜索"""
def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch2(alist[:midpoint], item)
            else:
                return binarySearch2(alist[midpoint+1:], item)

print(binarySearch2(testlist3, 33))