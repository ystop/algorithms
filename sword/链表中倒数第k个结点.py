# -*- coding:utf-8 -*-
# 输入一个链表，输出该链表中倒数第k个结点。
# 思路: 一个指针前进k个元素，双指针向前，一个指针到达后，另一个指针指向就是。（注意，k的有效性）
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0:
            return None
        h1 = head
        while k and h1 :
            h1 = h1.next
            k -= 1
        if k != 0:
            return None
        while h1:
            h1 = h1.next
            head = head.next
        return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
s = Solution()
print s.FindKthToTail(n1, 2).val