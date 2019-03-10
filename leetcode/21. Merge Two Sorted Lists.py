# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        ret = ListNode('None')
        cur = ret
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next

        while l1:
            cur.next = ListNode(l1.val)
            cur = cur.next
            l1 = l1.next

        while l2:
            cur.next = ListNode(l2.val)
            cur = cur.next
            l2 = l2.next

        return ret.next

    def p(self, head):
        while head:
            print head.val
            head = head.next

l1 = ListNode(-9)
l2 = ListNode(3)
l3 = ListNode(5)
l4 = ListNode(7)
l1.next = l2
l3.next = l4
s = Solution()
ret = s.mergeTwoLists(l1, l3)
s.p(ret)