# -*- coding:utf-8 -*-
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）

# 思路: 开个栈压数据，直到遇到pop的数相等。 如果相等的话，需要继续pop出来直到没有相等的或者为空。 如果stack/popv为空表示对
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[0]:
                popV.pop(0)
                stack.pop()
        return len(popV) == 0
s = Solution()
print s.IsPopOrder([1,2,3,4,5], [4,3,5,1,2])
print s.IsPopOrder([1,2,3,4,5], [4,5,3,2,1])