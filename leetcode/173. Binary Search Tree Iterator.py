# -*- coding:utf-8 -*-
# 思路：中序遍历，没别的。。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.data = []

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.data.append(node.val)
            node = node.right

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.data.pop(0)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.data) > 0

t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15 = TreeNode(15)
t7 = TreeNode(7)
t3.left = t9
t3.right = t20
t20.left = t15
t20.right = t7
# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(t3)
print obj.next()
print obj.hasNext()