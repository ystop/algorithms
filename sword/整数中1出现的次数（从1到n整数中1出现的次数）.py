# -*- coding:utf-8 -*-
# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
# 但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
# 思路:
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        mult, sumTimes = 1, 0
        while n//mult:
            div, mod = divmod(n, mult*10)
            curNum, curMod = divmod(mod, mult)
            if curNum > 1:
                sumTimes += div*mult + mult
            elif curNum == 1:
                sumTimes += div*mult + curMod + 1
            else:
                sumTimes += div*mult
            mult = mult*10
        return sumTimes

s = Solution()
s.NumberOf1Between1AndN_Solution(100)