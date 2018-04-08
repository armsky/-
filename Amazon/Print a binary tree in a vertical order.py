"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from Queue import Queue
from collections import defaultdict
class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        if not root:
            return []
        q = Queue()
        map = defaultdict(list)
        q.put((root, 0))
        while not q.empty():
            node, i = q.get()
            if node:
                map[i].append(node.val)
                q.put((node.left, i-1))
                q.put((node.right, i+1))
        return [map[i] for i in sorted(map.keys())]
