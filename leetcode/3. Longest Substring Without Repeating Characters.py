# -*- coding:utf-8 -*-
# 思路： 题目不算难，一个当前窗口，一个滑动结果。 遍历字符串，左右2个指针，如果右边指针不再窗口里，加入。 如果在，left到右边t出，再加入


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        ss = []
        ret = 0
        for i in range(0, len(s)):
            if s[i] not in ss:
                r = r + 1
            else:
                while s[i] in ss:
                    ss.pop(0)
                    l = l + 1

            ss.append(s[i])
            ret = max(ret, len(ss))
        return ret



s = Solution()
print s.lengthOfLongestSubstring("abcabca")