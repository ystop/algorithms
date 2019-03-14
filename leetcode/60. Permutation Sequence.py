# -*- coding:utf-8 -*-
# 思路:此题超时，看这个是遍历取，看起来是不可以的。TODO


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        path = []
        ret = []
        self.dfs(path, n, ret)
        return sorted(ret)[k-1]

    def dfs(self, path, n, ret):
        if len(path) == n:
            ret.append(''.join(path))
        for i in range(1, n + 1):
            i = str(i)
            if i in path:
                continue
            path.append(i)
            self.dfs(path, n, ret)
            path.pop()



s = Solution()
print s.getPermutation(9, 2678)