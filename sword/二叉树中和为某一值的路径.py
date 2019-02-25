# -*- coding:utf-8 -*-
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

# 思路: 递归到叶子节点。 如果为叶子节点且路径之和等于目标值，加入ret。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        ret = []
        path = []
        self._find(root, expectNumber, path, ret)
        return ret

    def _find(self, root, expectNumber, path, ret):
        path.append(root.val)
        if root.left is None and root.right is None and sum(path) == expectNumber:
            ret.append(path[:])
        if root.left:
            self._find(root.left, expectNumber, path, ret)
        if root.right:
            self._find(root.right, expectNumber, path, ret)
        path.pop()

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.left = t4
s = Solution()
print s.FindPath(t1, 3)