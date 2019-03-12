# -*- coding:utf-8 -*-
# 输入两个链表，找出它们的第一个公共结点。
# 思路: 获取长度，并截取对应的长度。 比较，第一个相等数据就是了。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l1 = self.getLength(pHead1)
        l2 = self.getLength(pHead2)
        if l1 > l2:
            for i in range(0, l1 - l2):
                pHead1 = pHead1.next
        else:
            for i in range(0, l2 - l1):
                pHead2 = pHead2.next

        while pHead1 and pHead2:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

    def getLength(self, list):
        c = 0
        while list:
            list = list.next
            c = c + 1
        return c
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l22 = ListNode(2)
l33 = ListNode(3)
l1.next = l2
l2.next = l3
l22.next = l33
s = Solution()
print s.FindFirstCommonNode(l1,l22)