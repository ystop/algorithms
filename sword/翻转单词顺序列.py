# -*- coding:utf-8 -*-
# 例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”
# 思路:空格隔开，一个一个反转
class Solution:
    def ReverseSentence(self, s):
        # write code here
        #return ' '.join(reversed(s.split(' ')))
        ss = s.split(' ')
        for i in ss:
            end = len(i) - 1
            start = 0
            i = list(i)
            while start < end:
                i[start], i[end] = i[end], i[start]
                start = start + 1
                end = end - 1
        return ' '.join(reversed(ss))