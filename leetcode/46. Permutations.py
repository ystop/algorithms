# -*- coding:utf-8 -*-
# 思路: 全部遍历，每个位置都有可能有是任何一个数据。 注意，如果在path里有了，就不要加入了。排序问题，(123)(321)都是


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        path = []
        self.dfs(nums, path, ret)
        return ret

    def dfs(self, nums, path, ret):
        if len(path) == len(nums):
            ret.append(path[:])
            return
        for i in nums:
            if i in path:
                continue
            path.append(i)
            self.dfs(nums, path, ret)
            path.pop()

s = Solution()
print s.permute([1, 2, 3])