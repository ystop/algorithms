# -*- coding:utf-8 -*-
# 思路: 最长公共前缀，取一个，去遍历其他的即可。

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        first = strs[0]
        others = strs[1:]
        retStr = ''
        for i in range(0, len(first)):
            flag = 0
            for j in range(0, len(others)):
                if i >= len(others[j]) or first[i] != others[j][i]:
                    flag = 1
            if flag == 0:
                retStr = retStr + first[i]
            else:
                break
        return retStr

s = Solution()
print s.longestCommonPrefix(["aca","cba"])