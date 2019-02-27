# -*- coding:utf-8 -*-
# 思路: 双指针，保存个最大的，一直比较就好了。   谁高度低，谁往中间靠。

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        maxWater = 0
        while start < end:
            nowWater = min(height[end], height[start]) * (end - start)
            maxWater = max(maxWater, nowWater)
            if height[start] < height[end]:
                start = start + 1
            else:
                end = end - 1
        return maxWater
s = Solution()
print s.maxArea([1,8,6,2,5,4,8,3,7])