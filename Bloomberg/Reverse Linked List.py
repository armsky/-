"""
Reverse a linked list.

Have you met this question in a real interview?
Example
For linked list 1->2->3, the reversed linked list is 3->2->1
"""
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if not head or not head.next:
            return head
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
