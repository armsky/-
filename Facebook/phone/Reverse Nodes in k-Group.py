"""
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in the
end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # 1 - 2 - 3 - 4 -5 - 6 - 7
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        start = dummy
        while start.next:
            end = start
            for i in range(k-1):
                end = end.next
                if not end.next:
                    return dummy.next
            rstart, rend = self.reverse(start.next, end.next)
            start.next = rstart
            start = rend

        return dummy.next


    def reverse(self, start, end):
        new = ListNode(None)
        new.next = start
        while new.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = new.next
            new.next = tmp
        return [end, start]
