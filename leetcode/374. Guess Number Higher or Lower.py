# -*- coding:utf-8 -*-
# 思路: 二分

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i <= j:
            mid = i + (j - i) / 2
            ret = guess(mid)
            if ret == 0:
                return mid
            elif ret == -1:
                j = mid - 1
            else:
                i = mid + 1
        return -1

s = Solution()
s.guessNumber(10)