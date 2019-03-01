# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t11 = TreeNode(1)
t22 = TreeNode(2)
t33 = TreeNode(4)
t1.left = t2
t11.right = t22
s = Solution()
print s.isSameTree(t1, t11)