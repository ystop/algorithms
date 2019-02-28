# -*- coding:utf-8 -*-
# 思路：和旋转数组很类似，双指针，记得走到最后的之前，然后旋转到前面就可以了。 注意特殊情况1.head为空 2.k比长度还大，k = k%c

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if not head:
            return head

        c = 0
        p = head
        while p:
            c = c + 1
            p = p.next
        k = k % c

        p1 = head
        p2 = head

        while k:
            p2 = p2.next
            k = k - 1

        if p2 is None:
            return head

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p2.next = head
        cur = p1.next


        p1.next = None
        return cur

    def p(self, head):
        while head:
            print head.val
            head = head.next

# l0 = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
# l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
s = Solution()
a = s.rotateRight(l1, 2)
s.p(a)