"""
Reverse a linked list from position m to n.

 Notice
Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

Have you met this question in a real interview?
Example
Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        m_pre = self.findkth(dummy, m-1)
        mth = m_pre.next
        nth = self.findkth(dummy, n)
        n_next = nth.next
        nth.next = None

        self.reverse(mth)
        m_pre.next = nth
        mth.next = n_next
        return dummy.next

    def findkth(self, head, k):
        cnt = 0
        while cnt < k:
            head = head.next
            cnt += 1
        return head

    def reverse(self, head):
        if not head or not head.next:
            return head
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
