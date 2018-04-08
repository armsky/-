"""
Convert a binary search tree to doubly linked list with in-order traversal.

Have you met this question in a real interview?
Example
Given a binary search tree:

    4
   / \
  2   5
 / \
1   3
return 1<->2<->3<->4<->5
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""


class Solution:
    head = None
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        if not root:
            return None
        self.helper(root)
        lhead = DoublyListNode(self.head.val)
        lnode = lhead
        tnode = self.head
        while lnode:
            lnode.next = DoublyListNode(tnode.right.val) if tnode.right else None
            lnode.prev = DoublyListNode(tnode.left.val) if tnode.left else None
            lnode = lnode.next
            tnode = tnode.right

        return lhead

    # Postorder recursive!!!
    def helper(self, root):
        if not root:
            return None
        self.helper(root.right)
        root.right = self.head
        if self.head is not None:
            self.head.left = root
        self.head = root
        self.helper(root.left)
