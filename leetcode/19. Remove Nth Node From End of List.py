# -*- coding:utf-8 -*-
# 思路:1. 双指针，p2先走到n,p1也开始走，p2.next到头，p1就是要删除的pre。 另外，注意走完p1就是None的情况，这种情况，说明，倒数第N个就是第一个元素，直接删了。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head

        while n:
            p1 = p1.next
            n = n - 1
        if not p1:
            head = head.next
            return head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
# l2.next = l3
s = Solution()
s.removeNthFromEnd(l1, 2)
