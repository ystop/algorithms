# -*- coding:utf-8 -*-
# 思路:  1. 二叉搜索树可以中序遍历，得到有序数组，在走一遍。（注意相等也需要false掉）
# 2. 二叉树的性质

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
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
        for i in range(0, len(ret) - 1):
            if ret[i] >= ret[i + 1]:
                return False
        return True

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t1
t2.right = t3
s = Solution()
print s.isValidBST(t1)