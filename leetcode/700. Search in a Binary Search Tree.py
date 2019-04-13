# -*- coding:utf-8 -*-
# 思路：二分查找

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        cur = root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return None

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t7 = TreeNode(7)
t4.left = t2
t2.left = t1
t2.right = t3
t4.right = t7
s = Solution()
print s.searchBST(t4, 2)
