# -*- coding:utf-8 -*-
# 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
# 思路：如代码
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return ''.join(list(reversed(list(reversed(s[:n])) + list(reversed(s[n:])))))

s = Solution()
print s.LeftRotateString("abcXYZdef", 3)