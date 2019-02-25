# -*- coding:utf-8 -*-
# 连续子数组的最大和
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return False
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
        return max(dp)


    def maxSubArray1(self, nums):
        if not nums:
            return False
        pre = nums[0]
        retMax = nums[0]
        for i in range(1, len(nums)):
            cur = max(pre + nums[i], nums[i])
            retMax = max(cur, retMax)
            pre = cur
        return retMax


s = Solution()

print s.maxSubArray([2, 3, -1, 400])