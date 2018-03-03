# -*-coding: utf-8 -*-
# Author: 
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :param nums:
        :return:
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    s = Solution()
    print(s.findDisappearedNumbers(nums))