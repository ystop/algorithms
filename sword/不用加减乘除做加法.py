# -*- coding:utf-8 -*-
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            sum = num1 ^ num2
            carry = 0xFFFFFFFF&(num1 & num2)<<1
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
            num1 = sum
            num2 = carry
        return num1
