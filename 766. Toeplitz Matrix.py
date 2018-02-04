# -*-coding: utf-8 -*-
# Author: 

class Solution:

    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] == matrix[i+1][j+1]:
                    return True
        return False

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(Solution().isToeplitzMatrix(matrix))