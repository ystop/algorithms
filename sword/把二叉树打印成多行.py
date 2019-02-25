# -*- coding:utf-8 -*-
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

# 思路:层序遍历,注意：每一次遍历需要先把结果存到ret里面去

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        ret = []
        queue = [pRoot]
        while queue:
            vals = []
            for val in queue:
                vals.append(val.val)
            ret.append(vals[:])

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
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
s = Solution()
print s.Print(t1)