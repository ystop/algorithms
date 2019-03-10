# -*- coding:utf-8 -*-
# 请实现两个函数，分别用来序列化和反序列化二叉树
# 思路: 遍历一遍存起来即可，取的时候一样。 前/中/后/层序 应该都可以（不存在写#)，还有前后(不需要写#)推树也可以。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if root:
            return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
        else:
            return '#'


    def Deserialize(self, s):
        s = s.split(',')
        return self.help(s)

    def help(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.help(list)
            root.right = self.help(list)
        return root
