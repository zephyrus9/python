
"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

import numpy as np 


class Solution:
	# solution 1
	def matrixshape(self, nums, r, c):
		try:
			return np.reshape(nums, (r, c)).tolist() # tolist()函数可以将数值或矩阵转换成列表
		except:
			return nums

	# solution 2

	def matrixshape2(self, nums, r, c):
		if r * c != len(nums) * len(nums[0]):
			return nums
		else:
			items = [y for x in nums for y in x]
			return [items[x*c: ((x+1)*c)] for x in range(r)]


if __name__ == '__main__':
	nums = [[1,2], [3,4]]
	r = 1
	c = 4
	print(Solution().matrixshape(nums, r, c))
	print(Solution().matrixshape2(nums, r, c))