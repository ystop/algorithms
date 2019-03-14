# -*- coding:utf-8 -*-
# 思路: 组合问题，注意边界，如果比target大,直接return; 由于是组合，记录start


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        ret = []
        start = 0
        self.dfs(candidates, start, path, ret, target)
        return ret

    def dfs(self, candidates, start, path, ret, target):
        if sum(path) > target:
            return
        if sum(path) == target:
            ret.append(path[:])
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.dfs(candidates, i, path, ret, target)
            path.pop()

s = Solution()
print s.combinationSum([2,3,5], 8)