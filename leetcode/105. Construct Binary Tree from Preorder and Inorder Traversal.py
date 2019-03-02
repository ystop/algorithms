# -*- coding:utf-8 -*-
# 思路: 经典题目，前中推树结构，根据前序和中序的规律，递归生成即可

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder and inorder:
            root = TreeNode(preorder[0])
            m = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:m+1], inorder[:m])
            root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
            return root
        else:
            return None

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

s = Solution()
ret = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
print s.levelOrder(ret)