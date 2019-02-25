# -*- coding:utf-8 -*-
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

# 思路: 1个栈，每次存2个数据，一个是最小，一个是当前数据，每次插入仍然需要计算最小。（或者1各栈存1个list，或者2个栈都是一个意思)
class Solution:
    def __init__(self):
        self.stack = []

    def push(self, node):
        # write code here
        min = self.min()
        if min is None or min > node:
            min = node
        self.stack.append(node)
        self.stack.append(min)
    def pop(self):
        # write code here
        if not self.stack:
            return None
        self.stack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-2]

    def min(self):
        # write code here
        if not self.stack:
            return None
        return self.stack[-1]

s = Solution()
s.push(3)
print s.min()