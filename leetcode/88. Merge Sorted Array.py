# -*- coding:utf-8 -*-
# 思路：题目要求必须在nums1,所以从后往前归并。

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        nn = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[nn] = nums2[j]
                j = j - 1
                nn = nn - 1
            else:
                nums1[nn] = nums1[i]
                i = i - 1
                nn = nn - 1

        # while i >= 0:
        #     nums1[nn] = nums1[i]
        #     nn = nn - 1
        #     i = i - 1

        while j >= 0:
            nums1[nn] = nums2[j]
            nn = nn - 1
            j = j - 1

        print nums1

s = Solution()
s.merge([4,5,6,0,0,0], 3, [1,2,3], 3)