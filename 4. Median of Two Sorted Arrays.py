# -*-coding: utf-8 -*-
# Author:


class Solution:

    def findMedianSortedArrays(self, num1, num2):
        """
        :param num1:
        :param num2:
        :return:
        """
        l = len(num1) + len(num2)
        print(l//2)
        return self.findKth(num1, num2, l//2) if l%2==1 else \
            (self.findKth(num1, num2,l//2 - 1) + self.findKth(num1, num2, l//2))/2

    def findKth(self, num1, num2 ,k):
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        if not num1:
            return num2[k]
        if k == len(num1) + len(num2) - 1:
            return max(num1[-1], num2[-1])
        i = len(num1) // 2
        j = k - i
        if num1[i] > num2[j]:
            return self.findKth(num1[:i], num2[j:], i)
        else:
            return self.findKth(num1[i:], num2[:j], j)


if __name__ == '__main__':
    num1 = []
    num2 = [2]
    print(Solution().findMedianSortedArrays(num1, num2))