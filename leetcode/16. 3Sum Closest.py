# -*- coding:utf-8 -*-
# 思路: 基本同3sum，排序，一次遍历fix一个数，双指针，每次维护2个遍历，一个是返回值，一个最小diff
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return False
        nums = sorted(nums)
        closet = nums[0] + nums[1] + nums[2]
        diff = abs(closet - target)
        for i in range(0, len(nums) - 1):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                tmpDiff = abs(nums[i] + nums[start] + nums[end] - target)
                if tmpDiff < diff:
                    closet = nums[i] + nums[start] + nums[end]
                    diff = tmpDiff

                if (nums[i] + nums[start] + nums[end]) > target:
                    end = end - 1
                elif (nums[i] + nums[start] + nums[end]) < target:
                    start = start + 1
                else:
                    start = start + 1
        return closet

s = Solution()
print s.threeSumClosest([-1, 2, 1, -4], 1)
print s.threeSumClosest([0, 0, 0], 1)
print s.threeSumClosest([1,2,4,8,16,32,64,128], 82)