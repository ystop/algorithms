# -*- coding:utf-8 -*-
# 思路：z字遍历

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        c = 1
        while queue:
            levelVal = []
            for i in queue:
                levelVal.append(i.val)
            if c & 1 == 0:
                levelVal.reverse()
            ret.append(levelVal)
            c = c + 1

            level = []
            for i in queue:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
            queue = level
        return ret

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
s = Solution()
print s.zigzagLevelOrder(t1)