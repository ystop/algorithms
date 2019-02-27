# -*- coding:utf-8 -*-
# 思路: 同3sum，先fix2个数，在双指针。。（target可以是负数，没法剪枝）
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        nums = sorted(nums)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    if (nums[i] + nums[j] + nums[start] + nums[end]) == target:
                        if [nums[i], nums[j], nums[start], nums[end]] not in ret:
                            ret.append([nums[i], nums[j], nums[start], nums[end]])
                        start = start + 1
                        end = end - 1
                    elif (nums[i] + nums[j] + nums[start] + nums[end]) > target:
                        end = end - 1
                    else:
                        start = start + 1
        return ret

s = Solution()
print s.fourSum([1,-2,-5,-4,-3,3,3,5], -11)