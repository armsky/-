"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support
the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
    otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache
    reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.pre = None

class LRUCache:
    '''
        Note: use a double linked list and dummy nodes for both head and tail.
    '''
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {} #{key: node}
        self.capacity = capacity
        self.head = Node(0,0) # dummy
        self.tail = Node(0,0) # dummy
        self.head.next = self.tail
        self.tail.pre = self.head

    # @return an integer
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.promote(node, new=False)
        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.cache:
            node = Node(key, value)
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.pre.key]
                self.tail.pre.pre.next = self.tail
                self.tail.pre = self.tail.pre.pre
            self.promote(node, new=True)
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            self.promote(node, new=False)

    def promote(self, node, new=True):
        if not new:
            node.pre.next = node.next
            node.next.pre = node.pre
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        node.pre = self.head
