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
        c = 1
        while fast < len(nums):
            if nums[fast] == nums[slow] and c == 0:
                fast = fast + 1
            else:
                slow = slow + 1
                nums[slow] = nums[fast]
                c = 1

            fast = fast + 1
        return nums

s = Solution()
print s.removeDuplicates([1,1,1,2,2,2,3])