# -*- coding:utf-8 -*-
# 思路：有序->每次取中间的作为根节点，两边是左右，递归下去就可以了

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) <= 0:
            return None
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

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
ret = s.sortedArrayToBST([-10,-3,0,5,9])
print s.levelOrder(ret)