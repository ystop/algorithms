# -*- coding:utf-8 -*-
# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

# 思路：中序遍历即可

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0:
            return None
        stack = []
        node = pRoot
        ret = []

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ret.append(node)
            node = node.right

        if k > len(ret):
            return None
        return ret[k - 1]

t8 = TreeNode(8)
t6 = TreeNode(6)
t10 = TreeNode(10)
t5 = TreeNode(5)
t7 = TreeNode(7)
t9 = TreeNode(9)
t11 = TreeNode(11)
t8.left = t6
t8.right = t10
t6.left = t5
t6.right = t7
t10.left = t9
t10.right = t11
s = Solution()
print s.KthNode(t8, 1)