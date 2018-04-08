"""
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two
lists and sorted in ascending order.

Have you met this question in a real interview?
Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
"""
class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    # Iterative version
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return dummy.next

    # Recursive version
     def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        root = ListNode(None)
        if l1.val < l2.val:
            root = l1
            root.next = self.mergeTwoLists(l1.next, l2)
        else:
            root = l2
            root.next = self.mergeTwoLists(l1, l2.next)
        return root
