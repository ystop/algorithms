# -*- coding:utf-8 -*-
# 思路: 栈的应用，每次入栈，出栈就可以了

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                print cur,i
                if i == ')' and cur == '(':
                    continue
                elif i == '}' and cur == '{':
                    continue
                elif i == ']' and cur == '[':
                    continue
                else:
                    return False
        return len(stack) == 0

s = Solution()
print s.isValid("}")