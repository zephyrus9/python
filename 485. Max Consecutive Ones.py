# -*-coding: utf-8 -*-
# Author: 

""" Discriptions

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :param nums:
        :return:
        """
        n = 0
        max_n = 0
        for s in nums:
            if s == 1:
                n += 1
            else:
                max_n = max(n, max_n)
                n = 0
        max_n = max(n, max_n)
        return max_n

    # 其他方法：
    def findmaxConsecutiveOnes_2(self, nums):
        return max(map(len, ''.join(map(str, nums)).split(0)))

# test
if __name__ == '__main__':
    nums = [1,0,1,1,1,1,0,0,1,1,1,0]
    s = Solution()
    print(s.findMaxConsecutiveOnes(nums))