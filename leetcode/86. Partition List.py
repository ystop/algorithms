# -*- coding:utf-8 -*-
# 思路: 题目说明相当不明确，实际上就是2个链表拼接。一个大于等于x的，一个小于的。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        cur = head
        list1 = ListNode('None')
        list2 = ListNode('None')
        bak1 = list1
        bak2 = list2
        while cur:
            if cur.val >= x:
                list2.next = ListNode(cur.val)
                list2 = list2.next
            else:
                list1.next = ListNode(cur.val)
                list1 = list1.next
            cur = cur.next
        ret = bak1
        while bak1.next:
            bak1 = bak1.next
        bak1.next = bak2.next
        return ret.next

    def p(self, l):
        while l:
            print l.val
            l = l.next

l1 = ListNode(1)
l4 = ListNode(4)
l3 = ListNode(3)
l2 = ListNode(2)
l5 = ListNode(5)
l22 = ListNode(2)
l1.next = l4
l4.next = l3
l3.next = l2
l2.next = l5
l5.next = l22
s = Solution()
l = s.partition(l1, 3)
s.p(l)