# -*- coding:utf-8 -*-
# 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
# 第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

# 思路:ht+list(维持顺序)
class Solution:
    # 返回对应char
    def __init__(self):
        self.ht = {}
        self.s = []

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.ht[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s.append(char)
        if char in self.ht:
            self.ht[char] += 1
        else:
            self.ht[char] = 1