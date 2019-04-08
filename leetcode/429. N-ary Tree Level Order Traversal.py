"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return root
        ret = []
        queue = [root]
        while queue:
            d = []
            for node in queue:
                d.append(node.val)
            ret.append(d)
            level = []
            for node in queue:
                for i in node.children:
                    level.append(i)
            queue = level
        return ret



n1 = Node(1, [])
n2 = Node(2, [])
n3 = Node(3, [])
n4 = Node(4, [])
n5 = Node(5, [])
n6 = Node(6, [])
n1.children = [n3, n2, n4]
n3.children = [n5, n6]
s = Solution()
print s.levelOrder(n1)
