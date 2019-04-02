# -*- coding:utf-8 -*-
# 思路: 1、暴力。m*n空间   遍历数组，如果值为1，遍历，当前行/当前列，置0.（注意：需要复制一个数组来判断是否是0）
# 2. m + n空间。 2个数组，row和clo，遍历记录某个数为0时，row和col的位置。 再次遍历，刷0
# 3. o(1)空间。 复杂度 m + n
# 先把第一行，第一列是否有0记录下来。
# 遍历除第一行，第一列的数据，如果为0，置第一行，第一列对应的位置为0
# 再次遍历，如果当前位置第一行/第一列有数据，则赋值为0.  最后，再根据一开始的记录，刷第一行/第一列。
import copy
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col1 = False
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                col1 = True
        row1 = False
        for j in range(0, len(matrix[0])):
            if matrix[0][j] == 0:
                row1 = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col1 == True:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0

        if row1 == True:
            for j in range(0, len(matrix[0])):
                matrix[0][j] = 0

        print matrix


    def setZeroesForce(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix1 = copy.deepcopy(matrix)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix1[i][j] == 0:
                    for k in range(0, len(matrix[0])):
                        matrix[i][k] = 0
                    for k in range(0, len(matrix)):
                        matrix[k][j] = 0
        print matrix


s = Solution()
# s.setZeroes([
#     [1,1,1],
#     [1,0,1],
#     [1,1,1],
#     [1,1,1]
# ])
s.setZeroes([
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
])