# -*- coding:utf-8 -*-
# 思路：层序遍历

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            levelVal = []
            for val in queue:
                levelVal.append(val.val)
            ret.append(levelVal[:])

            level = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
        return ret

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
s = Solution()
print s.levelOrder(t1)