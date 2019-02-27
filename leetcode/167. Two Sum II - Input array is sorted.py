# -*- coding:utf-8 -*-
# 思路: 1. 同2sum.  2.双指针，前后相加。
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j = j - 1
            elif numbers[i] + numbers[j] < target:
                i = i + 1
            else:
                return [i + 1, j + 1]
        return False

s = Solution()
print s.twoSum([-1,0], -1)