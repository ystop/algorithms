# -*- coding:utf-8 -*-
# 思路: 异或的性质

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        for i in range(1, len(nums)):
            ret = ret ^ nums[i]
        return ret

s = Solution()
s.singleNumber([2,2,1])