# -*- coding:utf-8 -*-
# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# 思路： 递归，比较左右即可

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self._compare(pRoot.left, pRoot.right)


    def _compare(self, p1, p2):
        if p1 is None and p2 is None:
            return True
        if p1 is None or p2 is None:
            return False
        if p1.val == p2.val:
            return self._compare(p1.left, p2.right) and self._compare(p1.right, p2.left)
        else:
            return False



t5 = TreeNode(5)
t2 = TreeNode(2)
t22 = TreeNode(2)
t3 = TreeNode(3)
t33 = TreeNode(3)
t4 = TreeNode(4)
t44 = TreeNode(4)
t1 = TreeNode(1)
t11 = TreeNode(1)
t5.left = t3
t5.right = t33
t3.left = t4
t33.right = t44
t4.left = t2
t44.right = t22
t2.left = t1
t22.right = t1

s = Solution()
print s.isSymmetrical(t5)
