# -*- coding:utf-8 -*-
# 统计一个数字在排序数组中出现的次数。

# 思路： 二分查找
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if data[mid] > k:
                left = mid + 1
            elif data[mid] < k:
                right = mid - 1
            else:
                c = 0
                pre = mid
                while pre >= left and data[pre] == k:
                    c = c + 1
                    pre = pre - 1
                post = mid + 1
                while post <= right and data[post] == k:
                    c = c + 1
                    post = post + 1
                return c
        return 0
s = Solution()
print s.GetNumberOfK([1,2,2,3,4,5], 2)