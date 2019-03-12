# -*- coding:utf-8 -*-
# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

# 思路: ht + list,ht存数据，list存顺序。
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ht = {}
        l = []
        for i in range(0, len(s)):
            if s[i] not in ht:
                ht[s[i]] = [i]
                l.append(s[i])
            else:
                ht[s[i]].append(i)
        for j in l:
            if len(ht[j]) == 1:
                return ht[j][0]
        return -1

s = Solution()
print s.FirstNotRepeatingChar('abcac')