# -*- coding:utf-8 -*-
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

# 思路: 1.递归 2.迭代

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        n1 = 1
        n2 = 2
        n3 = 3
        for i in range(3, number + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3


s = Solution()
print s.jumpFloor(10)