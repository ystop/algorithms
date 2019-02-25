# -*- coding:utf-8 -*-
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

# 思路:1.判断是否有环, 2.有环的话，一个指针从头走，双指针遇见就是了
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None
        slow = pHead
        fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None

        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n1
s = Solution()
print s.EntryNodeOfLoop(n1)