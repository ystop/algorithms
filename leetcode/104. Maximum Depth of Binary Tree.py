# -*- coding:utf-8 -*-
# 思路：递归计算出所有的深度，取最大即可。（或者一直滚动维护一个最大)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dept = []
        self._find(root, 1, dept)
        return max(dept)

    def _find(self, root, nowDept, dept):
        if root:
            if root.left is None and root.right is None:
                dept.append(nowDept)
            nowDept += 1
            self._find(root.left, nowDept, dept)
            self._find(root.right, nowDept, dept)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

t1.left = t2
t2.right = t3
s = Solution()
print s.maxDepth(t1)