# -*- coding:utf-8 -*-
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
# 思路 : 如果n1,n2相等，说明有可能。 如果返回失败，看左边，看右边。   里层比较的话，相等递归，不相等返回false，然后边界判断
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        ret = False
        if pRoot1.val == pRoot2.val:
            ret = self._check(pRoot1, pRoot2)
        if not ret:
            ret = self.HasSubtree(pRoot1.left, pRoot2)
        if not ret:
            ret = self.HasSubtree(pRoot1.right, pRoot2)
        return ret

    def _check(self, n1, n2):
        if n2 is None:
            return True
        if n1 is None:
            return False
        if n1.val == n2.val:
            return self._check(n1.left, n2.left) and self._check(n1.right, n2.right)
        else:
            return False

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5

t22 = TreeNode(2)
t44 = TreeNode(4)
t55 = TreeNode(5)
t22.left = t44
t22.right = t55
# t321 = TreeNode(321)
# t22.left = t321
s = Solution()
print s.HasSubtree(t1, t22)