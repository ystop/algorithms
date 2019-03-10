# -*- coding:utf-8 -*-
# 思路：二叉搜索树， 中序遍历，有序

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        ret = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            temp = stack.pop()
            ret.append(temp.val)
            node = temp.right
        return ret[k - 1]

t3 = TreeNode(3)
t1 = TreeNode(1)
t4 = TreeNode(4)
t2 = TreeNode(2)
# t3.left = t1
# t3.right = t4
# t1.right = t2
s = Solution()
print s.kthSmallest(t3,1)