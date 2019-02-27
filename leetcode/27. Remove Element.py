# -*- coding:utf-8 -*-
# 思路: 一个下标遍历，一个指针，往后读，如果不等于当前的，就赋值给记录的指针位置。

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
        return j


s = Solution()
print s.removeElement([3,3], 5)