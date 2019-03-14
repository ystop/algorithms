# -*- coding:utf-8 -*-
# 思路: 和subsets一样，多了排序去重

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        ret = []
        start = 0
        self._help(nums, start, path, ret)
        return ret

    def _help(self, nums, start, path, ret):
        if sorted(path[:]) not in ret:
            ret.append(sorted(path[:]))
        for i in range(start, len(nums)):
            path.append(nums[i])
            self._help(nums, i + 1, path, ret)
            path.pop()


s = Solution()
print s.subsetsWithDup([1,2,2])