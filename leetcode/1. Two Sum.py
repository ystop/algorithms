# -*- coding:utf-8 -*-
# 思路: hash表暂存
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(0, len(nums)):
            val = target - nums[i]
            if val not in ht:
                ht[nums[i]] = i
            else:
                return [ht[val], i]
        return False

s = Solution()
print s.twoSum([2, 7, 11, 15], 9)