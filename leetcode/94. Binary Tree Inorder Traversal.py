# -*- coding:utf-8 -*-
# 思路: 中序遍历..

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        node = root
        ret = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ret.append(node.val)
            node = node.right
        return ret


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3
s = Solution()
print s.inorderTraversal(t1)