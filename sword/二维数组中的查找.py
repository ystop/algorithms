#  -*- coding:utf-8 -*-
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 思路：右上角开始每次过滤一行或者一列

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False

        m = len(array) - 1
        n = len(array[0]) - 1
        i = 0
        j = n
        while i <= m and j >= 0:
            if array[i][j] > target:
                j = j - 1
            elif array[i][j] < target:
                i = i + 1
            else:
                return True
        return False

s = Solution()
print s.Find(
    5,
    [
        [1,2,3,4],
        [11,22,33,44]
    ]
)