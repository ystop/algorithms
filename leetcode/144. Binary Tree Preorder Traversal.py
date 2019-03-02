# -*- coding:utf-8 -*-
# 思路: 非递归中序遍历

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        node = root
        ret = []
        while stack or node:
            while node:
                ret.append(node.val)
                stack.append(node)
                node = node.left
            temp = stack.pop()
            node = temp.right
        return ret



t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15= TreeNode(15)
t7 = TreeNode(7)
t3.left = t9
t3.right = t20
t20.left = t15
t15.right = t7
s = Solution()
print s.preorderTraversal(t3)