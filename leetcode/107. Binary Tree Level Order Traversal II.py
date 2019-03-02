# -*- coding:utf-8 -*-
# 思路:  层序遍历一模一样，只是每次插入前面，而不是后面

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
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
            for i in queue:
                levelVal.append(i.val)
            ret.insert(0, levelVal)

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
print s.levelOrderBottom(t1)