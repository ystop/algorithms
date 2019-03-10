# -*- coding:utf-8 -*-
# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
# 要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        flag = 1
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                flag = -1
            s = s[1:]
        ret = 0
        temp = 1
        for i in reversed(list(s)):
            data = ord(i) - 48
            if data >= 0 and data <= 9:
                # print data, temp, data * temp
                ret = ret + data * temp
                temp = temp * 10
            else:
                return 0
        return ret * flag