# -*- coding:utf-8 -*-
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# 思路: 和数列是第一个意思。。 比如 2 * 4 假如竖着放，需要+f(3); 假如横着放，则下面必须也横着放，需要+f(2)
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
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