# -*- coding:utf-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 思路: fn = f(n-1) * 2
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        n = 2
        for i in range(3, number + 1):
            n = n * 2
        return n

