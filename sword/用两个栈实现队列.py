# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# 思路: 第一个栈存数据，pop数据把第一个栈的数据放到第二个栈里面去

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()



s = Solution()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
print s.pop()
print s.pop()