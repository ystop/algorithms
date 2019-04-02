# -*- coding:utf-8 -*-
# 思路: 先找到m的位置，每次把当前节点移动到m的后一个即可。 注意：一定要有个dummy节点。（如果没，第一个节点就需要反转，会发生问题）

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode('None')
        dummy.next = head
        pre = dummy

        t = m - 1
        while t > 0:
            pre = pre.next
            t = t - 1

        cur = pre.next
        t = n - m
        while t > 0:
            temp = cur.next
            tt = pre.next
            pre.next = temp
            cur.next = temp.next
            temp.next = tt
            t = t - 1
        return dummy.next

    def p(self, root):
        while root:
            print root.val
            root = root.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
s = Solution()
r = s.reverseBetween(l1, 2, 4)
s.p(r)