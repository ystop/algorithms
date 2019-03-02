# -*- coding:utf-8 -*-
# 思路: 同max，算出所有深度，求min

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dept = []
        self._getDept(root, 1, dept)
        return min(dept)

    def _getDept(self,root, curDep, dept):
        if root:
            if root.left is None and root.right is None:
                dept.append(curDep)

            curDep += 1
            self._getDept(root.left, curDep, dept)
            self._getDept(root.right, curDep, dept)


