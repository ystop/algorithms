# -*- coding:utf-8 -*-
# 思路:  递归找所有的path，求出sum，注意一个小点就是，cursum可以直接减去，不需要在加入一个参数


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        path = []
        self._getAllPath(root, sum, path, ret)
        return ret



    def _getAllPath(self, root, sum, path, ret):
        if not root:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            if sum == root.val:
                ret.append(path[:])

        self._getAllPath(root.left, sum - root.val, path, ret)
        self._getAllPath(root.right, sum - root.val, path, ret)

        path.pop()



t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15= TreeNode(15)
t7 = TreeNode(7)
t3.left = t9
t3.right = t20
t20.left = t15
t15.right = t7
s = Solution()
print s.pathSum(t3,12)