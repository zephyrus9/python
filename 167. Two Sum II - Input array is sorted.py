# -*-coding: utf-8 -*-
# Author: 
class Solution:
    def twoSum(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]

    # nums are sorted
    def twoSum2(self, nums, target):
        n, m = 0, len(nums) - 1
        while True:
            sum = nums[n] + nums[m]
            if sum > target:
                m -= 1
            elif sum == target:
                return [n+1, m+1]
            else:
                n =+ 1
if __name__ == '__main__':
    numbers = [2, 7, 11 ,15]
    target = 9
    print(Solution().twoSum2(numbers, target))