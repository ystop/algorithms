# -*- coding:utf-8 -*-
# 思路: 全部遍历，每个位置都有可能有是任何一个数据。 注意，如果在path里有了，就不要加入了。排序问题，(123)(321)都是
# 这个题目注意一下，要记录index，每个index可以用一次， 数据可以重复


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        ret = []
        self.dfs(nums, path, ret)
        return ret

    def dfs(self, nums, path, ret):
        if len(path) == len(nums):
            level = []
            for i in path:
                level.append(nums[i])
            if level not in ret:
                ret.append(level[:])
        for i in range(0, len(nums)):
            if i in path:
                continue
            path.append(i)
            self.dfs(nums, path, ret)
            path.pop()

s = Solution()
print s.permuteUnique([1,1,2])