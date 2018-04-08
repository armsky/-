"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        copyhead = RandomListNode(head.label)
        map = {head: copyhead}
        node = head
        copy = copyhead
        while node.next:
            nxt = RandomListNode(node.next.label)
            map[node.next] = nxt
            copy.next = nxt
            copy = copy.next
            node = node.next

        node = head
        while node:
            if node.random:
                map[node].random = map[node.random]
            node = node.next
        return copyhead
