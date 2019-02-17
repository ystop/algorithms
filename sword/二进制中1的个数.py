# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 思路: 1. 一位一位比，会死循环，可以解决（但是仍需要n次）
# 2. n & (n - 1) 会把最后一个1去掉，直到为0
class Solution:
    def NumberOf1(self, n):
        # write code here
        c = 0
        while n & 0xffffffff:
            n = n & (n - 1)
            c = c + 1
        return c

s = Solution()
print s.NumberOf1(7)