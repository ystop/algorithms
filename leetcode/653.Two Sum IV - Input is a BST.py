# -*- coding:utf-8 -*-
# 思路： 1. 中序遍历有序，可以双指针 2.直接ht+遍历递归(和二叉搜索树的条件没啥关系了)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        ht = {}
        return self._preOrder(root, k, ht)

    def _preOrder(self, root, k, ht):
        if root:
            target = k - root.val
            if target in ht:
                return True
            ht[root.val] = 1
            return self._preOrder(root.left, k, ht) or self._preOrder(root.right, k, ht)
        else:
            return False

# t5 = TreeNode(5)
# t3 = TreeNode(3)
# t6 = TreeNode(6)
# t2 = TreeNode(2)
# t4 = TreeNode(4)
# t7 = TreeNode(7)
# t5.left = t3
# t5.right = t6
# t3.left = t2
# t3.right = t4
# t6.right = t7
t2 = TreeNode(2)
t1 = TreeNode(1)
t3 = TreeNode(3)
# t2.left = t1
t2.right = t3
s = Solution()
print s.findTarget(t2, 6)