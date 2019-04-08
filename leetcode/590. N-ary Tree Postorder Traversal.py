# -*- coding:utf-8 -*-
# Definition for a Node.
#
# 思路:  递归/迭代,拆出来help方法好理解很多
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            for i in node.children:
                stack.append(i)
            ret.append(node.val)

        return ret[::-1]

    def postorderrecursive(self, root):
        ret = []
        if not root:
            return ret
        self.help(root, ret)
        return ret

    def help(self, root, ret):
        if root:
            for i in root.children:
                self.help(i, ret)
            ret.append(root.val)

n1 = Node(1, [])
n2 = Node(2, [])
n3 = Node(3, [])
n4 = Node(4, [])
n5 = Node(5, [])
n6 = Node(6, [])
n1.children = [n3, n2, n4]
n3.children = [n5, n6]
s = Solution()
print s.postorderrecursive(n1)
