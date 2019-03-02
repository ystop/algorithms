# -*- coding:utf-8 -*-
# 思路: 和 path sum是一个题目，求出来所有的路径，加起来就可以了

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        allSum = []
        nowSum = 0
        self._findPath(root, nowSum, allSum)
        return sum(allSum)

    def _findPath(self, root, nowSum, allSum):
        if not root:
            return
        nowSum = str(nowSum) + str(root.val)
        if root.left is None and root.right is None:
            allSum.append(int(nowSum))

        self._findPath(root.left, nowSum, allSum)
        self._findPath(root.right, nowSum, allSum)




t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
s = Solution()
print s.sumNumbers(t1)