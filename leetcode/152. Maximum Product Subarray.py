# -*- coding:utf-8 -*-
# 连续子数组的最大乘积
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return False
        dp_max = [nums[0]]
        dp_min = [nums[0]]
        for i in range(1, len(nums)):
            cur1 = dp_max[i - 1] * nums[i]
            cur2 = dp_min[i - 1] * nums[i]
            dp_max.append(max(cur1, cur2, nums[i]))
            dp_min.append(min(cur1, cur2, nums[i]))
        #print dp_max, dp_min
        return max(dp_max)

    def maxProductP(self, nums):
        if not nums:
            return False
        preMax = nums[0]
        preMin = nums[0]
        retMax = nums[0]
        for i in range(1, len(nums)):
            cur1 = preMax * nums[i]
            cur2 = preMin * nums[i]
            preMax = max(cur1, cur2, nums[i])
            preMin = min(cur1, cur2, nums[i])
            retMax = max(preMax, retMax)
        return retMax

s = Solution()
print s.maxProduct([2, 3, -2, 4])
