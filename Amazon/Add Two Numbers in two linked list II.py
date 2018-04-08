"""
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in forward order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

Have you met this question in a real interview?
Example
Given 6->1->7 + 2->9->5. That is, 617 + 295.

Return 9->1->2. That is, 912.
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
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    # NOTE: Version 2: add first and then create list. Note that python don't
    #       need care about int overflow. otherwise should convert to string first
    def addLists2(self, l1, l2):
        res1 = res2 = 0
        while l1:
            res1 = res1 * 10 + l1.val
            l1 = l1.next
        while l2:
            res2 = res2 * 10 + l2.val
            l2 = l2.next
        res = res1 + res2
        if res == 0:
            return ListNode(0)
        head = ListNode(0)
        while res:
            val = res % 10
            res /= 10
            nxt = head.next
            head.next = ListNode(val)
            head.next.next = nxt
            # head.next, head.next.next = ListNode(val), head.next # 3 in one line
        return head.next

    # NOTE: Version 1. use reversed linked list
    def addLists2(self, l1, l2):
        head = ListNode(0)
        node = head
        nl1 = self.reverse(l1)
        nl2 = self.reverse(l2)

        carry = 0
        while True:
            if nl1:
                carry += nl1.val
                nl1 = nl1.next
            if nl2:
                carry += nl2.val
                nl2 = nl2.next
            node.val = carry % 10
            carry /= 10
            if nl1 or nl2 or carry:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        return self.reverse(head)


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
