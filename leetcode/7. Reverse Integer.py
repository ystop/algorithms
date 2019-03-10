# -*- coding:utf-8 -*-
# 思路: 取余并整除原数，一直append到list即可

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            x = -x
            flag = 1
        ret = []
        while x:
            temp = x % 10
            x = x / 10
            ret.append(str(temp))
        if not ret:
            return 0

        ret = int(''.join(ret))
        if ret > pow(2, 31) - 1 or ret < -pow(2, 31):
            return 0
        if flag == 1:
            ret = -ret
        return ret


s = Solution()
print s.reverse(12)