"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe
its complexity.
"""
from heapq import heappop, heappush

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    # NOTE: Do not make change (head = head.next) in for loop
    def mergeKLists(self, lists):
        if not lists:
            return None
        q = []
        dummy_head = ListNode(None)
        for node in lists:
            if node:
                heappush(q, (node.val, node))
        cur = dummy_head
        while q:
            node = heappop(q)[1]
            if node.next:
                heappush(q, (node.next.val, node.next))
            cur.next = node
            cur = cur.next

        return dummy_head.next
