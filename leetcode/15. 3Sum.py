# -*- coding:utf-8 -*-
# 思路:1. fix一个数，然后ht，遍历。 2. fix一个数，然后双指针,注意去重,  剪枝(条件是等于0，可以剪枝，但是没这个条件，一定不可以）
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ret = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + nums[i] == 0:
                    if ([nums[i], nums[start], nums[end]]) not in ret:
                        ret.append(([nums[i], nums[start], nums[end]]))
                    start = start + 1
                    end = end - 1
                elif nums[start] + nums[end] + nums[i] > 0:
                    end = end - 1
                else:
                    start = start + 1
        return ret

s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])