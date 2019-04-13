# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ret = []
        pre = None
        curNum = 1
        maxNum = 1
        while stack:
            node = stack.pop()
            # print pre, node.val,maxNum
            if pre == node.val:
                curNum = curNum + 1
            else:
                curNum = 1

            if curNum > maxNum:
                maxNum = curNum
                ret = [node.val]
            elif curNum == maxNum:
                ret.append(node.val)
            else:
                pass

            pre = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ret


t1 = TreeNode(1)
# t2 = TreeNode(2)
# t22 = TreeNode(2)
# t1.right = t2
# t2.left = t22

#
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t10 = TreeNode(10)
# t5 = TreeNode(5)
# tf3 = TreeNode(-3)
# t11 = TreeNode(11)
# t33 = TreeNode(3)
# tf2 = TreeNode(-2)
# t10.left = t5
# t10.right = tf3
# t5.left = t3
# t5.right = t2
# t3.left = t33
# t3.right = tf2
# t2.right = t1
# t10.right = tf3
# tf3.right = t11

s = Solution()
print s.findMode(t1)