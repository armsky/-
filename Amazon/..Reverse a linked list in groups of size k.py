"""
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end
should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

Have you met this question in a real interview?
Example
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        start = head

        while start.next:
            end = start
            for i in range(k-1): # need make sure last end.next is not None, so only iterate k-1 times.
                end = end.next
                if end.next is None:
                    return dummy.next
            res = self.reverse(start.next, end.next) # not end but end.next
            start.next = res[0]
            start = res[1]
        return dummy.next

    def reverse(self, start, end):
        newhead=ListNode(0)
        newhead.next=start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]
