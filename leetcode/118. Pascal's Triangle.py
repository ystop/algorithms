# -*- coding:utf-8 -*-
# 思路：第一个手动初始化，第二层开始手动补收尾的1，中间的是上一层的2个之和

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ret = [[1]]
        if numRows == 1:
            return ret
        for i in range(1, numRows):
            level = [1]
            for j in range(1, i):
                level.append(ret[i-1][j-1] + ret[i-1][j])
            level.append(1)
            ret.append(level)
        return ret

s = Solution()
print s.generate(5)