# -*- coding:utf-8 -*-
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39

# 思路: 1. 递归 2. 迭代
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        n0 = 0
        n1 = 1
        n2 = -1
        for i in range(2, n + 1):
            n2 = n0 + n1
            n0 = n1
            n1 = n2
        return n2

s = Solution()
print s.Fibonacci(10)
