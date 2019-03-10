# -*- coding:utf-8 -*-
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 思路：类似2sum，排序后且要求乘积最小，双指针
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        i = 0
        j = len(array) - 1
        ret = []
        while i < j:
            if array[i] + array[j] == tsum:
                ret.append(array[i])
                ret.append(array[j])
                break
            elif array[i] + array[j] > tsum:
                j = j - 1
            else:
                i = i + 1
        return ret
s = Solution()
print s.FindNumbersWithSum([1,2,4,7,11,16],5)