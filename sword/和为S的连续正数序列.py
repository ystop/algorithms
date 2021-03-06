# -*- coding:utf-8 -*-
# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
# 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

# 思路，序列肯定至少2个，所以最多需要遍历到一半，暴力加起来算。
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []
        ret = []
        i = 1
        j = 2
        while i < j and i <= tsum >> 1:
            sum = (i + j) * (j - i + 1) >> 1
            # print i, j, sum
            if sum == tsum:
                ret.append(range(i, j + 1))
                i = i + 1
            elif sum < tsum:
                j = j + 1
            elif sum > tsum:
                i = i + 1
        return ret