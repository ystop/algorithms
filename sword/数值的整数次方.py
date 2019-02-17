# -*- coding:utf-8 -*-
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 思路: exponent为负数情况特殊考虑。递归算,log

class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent < 0:
            return 1 / self._power(base, -exponent)
        return self._power(base, exponent)

    def _power(self, base, exponent):
        if exponent == 1:
            return base
        result = self._power(base, exponent >> 1)
        if exponent & 1 == 1:
            result = result * result * base
        else:
            result = result * result
        return result

s = Solution()
print s.Power(2, 10)