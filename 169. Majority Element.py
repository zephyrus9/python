# -*-coding: utf-8 -*-
# Author: 
class Solution:
    def majorityElement(self, nums):

        return sorted(nums)[len(nums)//2]


if __name__ == '__main__':
    s = [1,2,23,21,2,2,2,1,2,3,2,3,2,2,2,43,2,23,2]
    print(Solution().majorityElement(s))

    # run time
    from timeit import timeit
    print(timeit(lambda: Solution().majorityElement(s)))