# -*-coding: utf-8 -*-
# Author: 
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :param nums: List[int]
        :return: void Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    print(s.moveZeroes(nums))