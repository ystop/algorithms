# -*- coding:utf-8 -*-
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
# 因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

# 思路：dfs搜索，注意的是visited是需要持久的，不可以pop
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        ret = []
        visited = []
        self._dfs(0, 0, threshold, rows, cols, visited, ret)
        return len(ret)

    def _dfs(self, i, j, threshold, rows, cols, visited, ret):
        if i >= 0 and j >= 0 and i < rows and j < cols:
            if self.checkAuth(threshold, i, j):
                if [i, j] not in visited:
                    ret.append([i, j])
                    visited.append([i, j])
                    self._dfs(i + 1, j, threshold, rows, cols, visited, ret)
                    self._dfs(i - 1, j, threshold, rows, cols, visited, ret)
                    self._dfs(i, j + 1, threshold, rows, cols, visited, ret)
                    self._dfs(i, j - 1, threshold, rows, cols, visited, ret)
                    # visited.pop()

    def checkAuth(self, threshold, m, n):
        m1 = 0
        while m:
            m1 = m1 + m % 10
            m = m / 10
        n1 = 0
        while n:
            n1 = n1 + n % 10
            n = n / 10

        return n1 + m1 <= threshold

s = Solution()
print s.movingCount(5, 10, 10)