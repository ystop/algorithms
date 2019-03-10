# -*- coding:utf-8 -*-
# 思路：斐波那契数列

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        n1 = 1
        n2 = 2
        n3 = 3
        for i in range(3, n+1):
            n3 = n2 + n1
            n1 = n2
            n2 = n3
        return n3


s = Solution()
print s.climbStairs(4)