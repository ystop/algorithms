# -*- coding:utf-8 -*-
# 思路：依然是层序遍历，每次去左右边的数据即可。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            level = []
            ret.append(queue[-1].val)
            for i in queue:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
            queue = level
        return ret




t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15= TreeNode(15)
t7 = TreeNode(7)
t3.left = t9
t3.right = t20
t20.left = t15
t20.right = t15
s = Solution()
print s.rightSideView(t3)