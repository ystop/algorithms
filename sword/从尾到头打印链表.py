# -*- coding:utf-8 -*-
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# 思路:
# 1. 用辅助空间，栈，记录下来
# 2. 直接反转链表，然后读一遍。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        pre = None
        cur = listNode
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        ret = []
        while pre:
            ret.append(pre.val)
            pre = pre.next
        return ret

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
s = Solution()
print s.printListFromTailToHead(n1)
