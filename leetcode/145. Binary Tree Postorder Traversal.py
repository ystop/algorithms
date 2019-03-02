# -*- coding:utf-8 -*-
# 思路：后序遍历用一个栈，反过来存，最后把结果一反

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        ret.reverse()
        return ret

t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15 = TreeNode(15)
t7 = TreeNode(7)
t3.left = t9
t3.right = t20
t20.left = t15
t20.right = t7
s = Solution()
print s.postorderTraversal(t3)