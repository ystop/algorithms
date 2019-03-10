# -*- coding:utf-8 -*-
# 思路: 查找旋转数组中的数据 1. 跳出条件是等于目标数了，然后mid分为右边有序和左边有序（等号放任何一个都可以） 然后每一种情况 分为target在有序的这边
# 还是不有序的那边，从而计算start,end

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] > nums[end]:
                if nums[mid] > target and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1



s = Solution()
print s.search([4,5,6,7,0,1,2], 3)