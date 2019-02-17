# -*- coding:utf-8 -*-
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
class Solution:
    def reOrderArray(self, array):
        # write code here
        s1 = []
        s2 = []
        for i in array:
            if i % 2 == 0:
                s2.append(i)
            else:
                s1.append(i)
        return s1 + s2

s = Solution()
s.reOrderArray([1])