# -*- coding:utf-8 -*-
# 思路: 题目要求不可以改链表，因此可以用栈存。
# 2个栈存储数据，遍历即可。注意，head每次插入头结点，如果插入的是尾节点，需要reverse一下。

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
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        next = 0
        head = ListNode('None')
        ret = head
        while stack1 or stack2:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            temp = v1 + v2 + next
            cur = temp % 10
            next = temp / 10
            head.next = ListNode(cur)
            head = head.next
        if next:
            head.next = ListNode(next)
        return self.reverse(ret.next)

    def reverse(self, l):
        pre = None
        cur = l
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        next = 0
        head = ListNode('None')
        ret = head
        while stack1 or stack2:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            temp = v1 + v2 + next
            cur = temp % 10
            next = temp / 10
            node = ListNode(cur)
            pre = head.next
            head.next = node
            node.next = pre
            head = head
        if next:
            node = ListNode(next)
            pre = head.next
            head.next = node
            node.next = pre
            head = head
        return ret.next


    def p(self, i):
        while i:
            print i.val
            i = i.next



s = Solution()
l7 = ListNode(7)
l2 = ListNode(2)
l4 = ListNode(4)
l3 = ListNode(3)
l5 = ListNode(5)
l6 = ListNode(6)
l44 = ListNode(4)
l7.next = l2
l2.next = l4
l4.next = l3
l5.next = l6
l6.next = l44
ret = s.addTwoNumbers1(l7, l5)
s.p(ret)