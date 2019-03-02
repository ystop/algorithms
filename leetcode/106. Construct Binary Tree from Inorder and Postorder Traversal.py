# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            root = TreeNode(postorder[-1])
            m = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:m], postorder[:m])
            root.right = self.buildTree(inorder[m+1:], postorder[m:len(postorder) - 1])
            return root
        else:
            return None
