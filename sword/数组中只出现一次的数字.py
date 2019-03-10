# -*- coding:utf-8 -*-
# 一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

# 思路：到最后还是要1组数据里面异或，得到结果。问题是怎么拆？
# 首先，全部异或，得到2个数的异或结果（一定有一位是为1的）。
# 再寻找倒数第一个为1位的，记录下来偏移index。
# 再把原始数据 每个数据都偏移index，如果为1，则进a，如果不为1，则进b。
# 最后在把a都异或，b都异或。

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ret = array[0]
        for i in range(1, len(array)):
            ret = ret ^ array[i]

        index = 0
        while ret:
            r = ret & 1
            if r == 1:
                break
            else:
                index = index + 1
            ret = ret >> 1

        a1 = []
        a2 = []
        for i in range(0, len(array)):
            if (array[i] >> index ) & 1 == 0:
                a1.append(array[i])
            else:
                a2.append(array[i])

        ret1 = a1[0]
        for i in range(1, len(a1)):
            ret1 = ret1 ^ a1[i]
        ret2 = a2[0]
        for i in range(1, len(a2)):
            ret2 = ret2 ^ a2[i]
        return [ret1, ret2]

s = Solution()
print s.FindNumsAppearOnce([1,2,2,3,3,5])