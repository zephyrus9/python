# -*-coding: utf-8 -*-
# Author:
import math


'''
1. 利用递归的思想将将整数转换成任意进制表示的字符串形式
'''
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]

print(to_str(1024, 2))


'''
2. 利用递归的思想将字符串反向输出，
'''
def myReverse(items):
     if len(items) < 1:
         return items
     else:
         return myReverse(items[1:]) + items[0]

print(myReverse('asdfghk'))

'''
3. 判断是否为回文
'''
def func(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return func(string[1:-1])

print(func('assa'))

# 更为简洁的方法：
def func2(string):
    return s == s[::-1]
print(func('sdsdssdsds'))

"""
4. 用递归实现斐波那契数列
"""
def fib_recur(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recur(n-1) + fib_recur(n-2)

print(fib_recur(9))

"""
5. 递归计算阶乘
"""
def f(num):
    if num == 0:
        return 1
    else:
        return num * f(num - 1)
print(f(4))