# -*- coding:utf-8 -*-
# 思路:  数组相加

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        next = 0
        ret = []
        while i >= 0 or j >= 0:
            v1 = 0
            v2 = 0
            if i >= 0:
                v1 = num1[i]
                i = i - 1
            if j >= 0:
                v2 = num2[j]
                j = j - 1
            temp = next + int(v1) + int(v2)
            cur = temp % 10
            next = temp / 10
            ret.insert(0, str(cur))
        if next:
            ret.insert(0, str(next))
        return ''.join(ret)



s = Solution()
print s.addStrings('99','9')