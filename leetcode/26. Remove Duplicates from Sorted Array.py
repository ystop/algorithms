# -*- coding:utf-8 -*-
# 思路: 有序数组，题目要求前面是不重复的元素，并返回有几个数（下标+1）。 思路双指针，交换。

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        return slow + 1

s = Solution()
print s.removeDuplicates([1,1,2])
# print s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])