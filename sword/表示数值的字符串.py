# -*- coding:utf-8 -*-
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
#  但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

# 思路，特殊的字符发现了就错
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        isAllowDot = True
        isAllowE = True
        for i in range(len(s)):
            if s[i] in "+-" and (i==0 or s[i-1] in "eE") and i < len(s)-1:
                continue
            elif isAllowDot and s[i] == ".":
                isAllowDot = False
                if i >= len(s)-1 or s[i+1] not in "0123456789":
                    return False
            elif isAllowE and s[i] in "Ee":
                isAllowDot = False
                isAllowE = False
                if i >= len(s)-1 or s[i+1] not in "0123456789+-":
                    return False
            elif s[i] not in "0123456789":
                return False
        return True