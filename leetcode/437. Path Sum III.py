# -*- coding:utf-8 -*-
# 思路：双递归，外层是 当前+左+右边。  里层是计算数量的。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        else:
            return 0

    def dfs(self, root, sum):
        s = 0
        if not root:
            return s
        if root.val == sum:
            s = s + 1
        s = s + self.dfs(root.left, sum - root.val)
        s = s + self.dfs(root.right, sum - root.val)
        return s

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t10 = TreeNode(10)
t5 = TreeNode(5)
tf3 = TreeNode(-3)
t11 = TreeNode(11)
t33 = TreeNode(3)
tf2 = TreeNode(-2)
t10.left = t5
t10.right = tf3
t5.left = t3
t5.right = t2
t3.left = t33
t3.right = tf2
t2.right = t1
t10.right = tf3
tf3.right = t11
s = Solution()
print s.pathSum(t10, 8)