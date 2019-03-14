# -*- coding:utf-8 -*-
# 思路：丑数，如果可以整除5，2，3一直整除。

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 5 == 0:
            num = num / 5
        while num % 3 == 0:
            num = num / 3
        while num % 2 == 0:
            num = num / 2
        if num == 1:
            return True
        else:
            return False

s = Solution()
print s.isUgly(5)