# -*- coding:utf-8 -*-
# 思路: 有序数组，c记录几次，如果不相等，交换，并重置c；如果相等，且c次数用完，fast继续；如果相等，但是c有次数，slow往前继续走，c-1

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        slow = 0
        fast = 1
        c = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]
                c = 1
            else:
                if c == 0:
                    pass
                else:
                    slow = slow + 1
                    nums[slow] = nums[fast]
                    c = c - 1
            fast = fast + 1
        print nums
        return slow + 1


s = Solution()
print s.removeDuplicates([0,0,1,1,1,1,2,3,3])
print s.removeDuplicates([1,1,1,2,2,3])
print s.removeDuplicates([1])
print s.removeDuplicates([1,2])