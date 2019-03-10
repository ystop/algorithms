# -*- coding:utf-8 -*-
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
#  例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

# 思路: 一个pre，一个cur跑。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        cur = pHead
        pre = ListNode('None')
        pre.next = cur
        ret = pre
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return ret.next

    def p(self, head):
        while head:
            print head.val
            head = head.next

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(1)
l33 = ListNode(1)
l4 = ListNode(1)
l44 = ListNode(1)
l5 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l33
l33.next = l4
l4.next = l44
l44.next = l5
s = Solution()
a = s.deleteDuplication(l1)
s.p(a)