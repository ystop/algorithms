# -*- coding:utf-8 -*-
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。
# 求按从小到大的顺序的第N个丑数。

# 思路: 假设集合中已经有若干个丑数排好序后放在集合中，并且把已有最大的丑数记做M，我们接下来分析如何生成下一个丑数。
# 该丑数肯定是前面某一个丑数乘以2、3或者5的结果，我们首先考虑把已有的丑数乘以2、3和5，然后通过比较三个数的大小，
# 找出三个树中最小的丑数存入集合。为了避免重复，如果最小的丑数等于乘以2的结果，i2++；
# 如果最小的丑数等于乘以3的结果，i3++;如果最小的丑数等于乘以5的结果，i5++（i2、i3和i5是集合的索引且初值为0，首先集合存入1）。
# 这样得到的丑数在集合中是按照从小到大排序的。

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return False
        if index == 1:
            return 1
        ret = [1]
        m2 = 0
        m3 = 0
        m5 = 0
        i = 1
        while i < index:
            next = min(ret[m2] * 2, ret[m3] * 3, ret[m5] * 5)
            ret.append(next)
            if ret[m2] * 2 == next:
                m2 = m2 + 1
            if ret[m3] * 3 == next:
                m3 = m3 + 1
            if ret[m5] * 5 == next:
                m5 = m5 + 1
            i = i + 1
        return ret[-1]

s = Solution()
print s.GetUglyNumber_Solution(5)