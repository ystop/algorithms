# -*- coding:utf-8 -*-
# 思路: 3指针，1遍历指针 2 红指针 3 蓝指针。 读一遍

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                i = i + 1
                start = start + 1
            elif nums[i] == 1:
                i = i + 1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end = end - 1
        print nums

s = Solution()
s.sortColors([0,1,0])