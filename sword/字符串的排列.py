# -*- coding:utf-8 -*-
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

# 思路：深搜，全搜，最后去重。每次fix一位，再遍历另外的。
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        path = []
        ret = []
        self.help(ss, path, ret)
        return sorted(list(set(ret)))

    def help(self, ss, path, ret):
        print ss, path, ret
        if not ss:
            ret.append(''.join(path))
        for i in range(0, len(ss)):
            self.help(ss[:i] + ss[i+1:], path + [ss[i]], ret)
s = Solution()
print s.Permutation('abc')