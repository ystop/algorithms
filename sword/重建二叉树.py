# -*- coding:utf-8 -*-
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

# 思路: 根据规律，如果前序/中序为空，则是空节点返回None;否则获取前序第一个的元素必定是根节点，获取到在中序的位置，分开左右数据，递归进行。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        rootIndex = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:1 + rootIndex], tin[:rootIndex])
        root.right = self.reConstructBinaryTree(pre[1 + rootIndex:], tin[rootIndex + 1:])
        return root

s = Solution()
print s.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])

