# -*- coding:utf-8 -*-
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 思路：遍历树，判断树的左右深度是否小于1即可。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.getDepth(pRoot.left) - self.getDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and \
        self.IsBalanced_Solution(pRoot.right)



    def getDepth(self, pRoot):
        if pRoot is None:
            return 0
        return max(self.getDepth(pRoot.left), self.getDepth(pRoot.right)) + 1