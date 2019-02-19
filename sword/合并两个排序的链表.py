# -*- coding:utf-8 -*-
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# 思路: 类似2个数组归并的过程

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        cur = ListNode('None')
        bak = cur
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                cur.next = pHead2
                pHead2 = pHead2.next
            else:
                cur.next = pHead1
                pHead1 = pHead1.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2
        return bak.next

    def p(self, node):
        while node:
            print node.val
            node = node.next

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n11 = ListNode(11)
n22 = ListNode(22)
n11.next = n22
s = Solution()
n = s.Merge(n1, n11)
s.p(n)

