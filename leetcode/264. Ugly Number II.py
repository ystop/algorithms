# -*- coding:utf-8 -*-
# 思路: 丑数，同sword，每次肯定是m2,m3,m5乘积中的最小，为了保证ret有序，比较相等后，把对应的位置+1

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        m2 = 0
        m3 = 0
        m5 = 0
        ret = [1]
        i = 1
        while i < n:
            next = min(ret[m2] * 2, ret[m3] * 3, ret[m5] * 5)
            ret.append(next)
            if ret[m2] * 2 == next:
                m2 += 1
            if ret[m3] * 3 == next:
                m3 += 1
            if ret[m5] * 5 == next:
                m5 += 1
            i = i + 1
        return ret[-1]
s = Solution()
print s.nthUglyNumber(5)