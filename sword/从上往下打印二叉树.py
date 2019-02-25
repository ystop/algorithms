# -*- coding:utf-8 -*-
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
# 思路:层序遍历
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            level = []
            for node in queue:
                ret.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
        return ret

