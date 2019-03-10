# -*- coding:utf-8 -*-
# 思路: 2个链表依次相加，注意1. 进位的问题。  2.结束后next还存在的情况
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next = 0
        head = ListNode('None')
        ret = head
        while l1 or l2:
            l1val = 0
            l2val = 0
            if l1:
                l1val = l1.val
            if l2:
                l2val = l2.val
            now = l1val + l2val + next
            next = now / 10
            now = now % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head.next = ListNode(now)
            head = head.next
        if next:
            head.next = ListNode(next)
        return ret.next

    def p(self, head):
        while head:
            print head.val
            head = head.next

l2 = ListNode(2)
l4 = ListNode(4)
l3 = ListNode(3)
l2.next = l4
l4.next = l3


l5 = ListNode(5)
l6 = ListNode(6)
l4 = ListNode(4)
l5.next = l6
l6.next = l4

s = Solution()
ret = s.addTwoNumbers(l2, l5)
s.p(ret)