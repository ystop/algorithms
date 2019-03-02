# -*- coding:utf-8 -*-
# 思路:  前序遍历，求每一个元素的左右子树的深度看绝对值。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
                return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

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
print s.isBalanced(t3)