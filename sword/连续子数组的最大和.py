# -*- coding:utf-8 -*-
# HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
# 当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢
# ？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

# 思路: 1. 一个dp数组，维护当前位置最大的连续子序列和。 2. 优化1,用2个变量,一个是当前cur,一个是max，遍历一遍取max
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [array[0]]
        for i in range(1, len(array)):
            dp.append(max(dp[i - 1] + array[i], array[i]))
        return max(dp)

    def FindGreatestSumOfSubArrayP(self, array):
        # write code here
        m = array[0]
        c = array[0]
        for i in range(1, len(array)):
            c = max((c + array[i]), array[i])
            m = max(c, m)
        return m



s = Solution()
print s.FindGreatestSumOfSubArrayP([2, 3, -2, 4])