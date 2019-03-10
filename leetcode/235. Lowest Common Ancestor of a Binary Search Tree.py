# -*- coding:utf-8 -*-
# 思路: 求出p,q的最大和最小，如果正好再中间，则是，否则，看左右。 2种方法 递归/迭代

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            mins = min(p.val, q.val)
            maxs = max(p.val, q.val)

            if root.val >= mins and root.val <= maxs:
                return root
            if root.val < mins:
                return self.lowestCommonAncestor(root.right, p, q)
            if root.val > maxs:
                return self.lowestCommonAncestor(root.left, p, q)
        else:
            return False

    def lowestCommonAncestorIter(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        mins = min(p.val, q.val)
        maxs = max(p.val, q.val)
        while root:
            if root.val >= mins and root.val <= maxs:
                return root
            if root.val < mins:
                root = root.right
            if root.val > maxs:
                root = root.left
        return root

t6 = TreeNode(6)
t2 = TreeNode(2)
t8 = TreeNode(8)
t0 = TreeNode(0)
t4 = TreeNode(4)
t7 = TreeNode(7)
t9 = TreeNode(9)
t3 = TreeNode(3)
t5 = TreeNode(5)

t6.left = t2
t6.right = t8
t2.left = t0
t2.right = t4
t4.left = t3
t4.right = t5
t8.left = t7
t8.right = t9

s = Solution()
print s.lowestCommonAncestor(t6, t2, t8)