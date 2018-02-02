# -*-coding: utf-8 -*-
# Author: 
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
# Definition for singly-linked list.


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        l = result

        while l1 or l2:
            result.var = result.val + self.addnodes(l1, l2)
            if result.val < 10:
                if l1 and l1.next or l2 and l2.next:
                    l.next = ListNode(0)

            else:
                result.val -= 10
                result.next = ListNode(1)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
            result = result.next

        return result

    def addnodes(self, node1, node2):
        if not node1 and not node2:
            raise Exception("two nodesa are None")
        if not node1:
            return node2.val
        if not node2:
            return node1.val
        return node1.val + node2.val

if __name__ == '__main__':
    l1 = ['1','2','3']
    l2 = ['3','4','5']
    s = Solution()
    s.addTwoNumbers(l1, l2)
