# Definition for a binary tree node.
# 判断二叉树是否是镜像

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self._compare(root.left, root.right)

    def _compare(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        if n1.val == n2.val:
            return self._compare(n1.left, n2.right) and self._compare(n1.right, n2.left)
        else:
            return False
