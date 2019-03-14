# -*- coding:utf-8 -*-
# # 思路:遍历，注意相对顺序变了，算同一个。 所以 123,321是同一个。 组合问题，所以注意记录下开始的index

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        path = []
        start = 1
        self.dfs(n, k, start, path, ret)
        return ret

    def dfs(self, n, k, start, path, ret):
        if len(path) > k:
            return
        if len(path) == k:
            ret.append(path[:])
        for i in range(start, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, path, ret)
            path.pop()

s = Solution()
print s.combine(4, 2)