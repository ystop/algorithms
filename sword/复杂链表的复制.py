# -*- coding:utf-8 -*-
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

# 思路: 遍历一遍链表，每次多生成一个相同节点(只复制label和next)。 再次遍历，复制random。 再次遍历，取出复制出来的这串新节点。
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        cloNode = pHead
        while cloNode:
            node = RandomListNode(cloNode.label)
            node.next = cloNode.next
            cloNode.next = node
            cloNode = node.next
        cloNode = pHead
        while cloNode:
            node = cloNode.next
            if cloNode.random:
                node.random = cloNode.random.next
            cloNode = node.next
        cloNode = pHead
        pHead = pHead.next
        while cloNode.next:
            node = cloNode.next
            cloNode.next = node.next
            cloNode = node
        return pHead

