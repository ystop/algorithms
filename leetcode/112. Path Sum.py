# -*- coding:utf-8 -*-
# 思路：遍历所有的叶子，看是否等于sum

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ret = self._check(root, 0, sum)
        return ret


    def _check(self, root, nowSum, sum):
        if not root:
            return False
        nowSum = nowSum + root.val
        if root.left is None and root.right is None:
            if nowSum == sum:
                return True
            else:
                return False
        else:
            l = self._check(root.left, nowSum, sum)
            r = self._check(root.right, nowSum, sum)
            return l or r

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
print s.hasPathSum(t3,13)