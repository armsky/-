"""
Find the distance between two keys in a binary tree, no parent pointers are given.
Distance between two nodes is the minimum number of edges to be traversed to reach
one node from other.
"""

#NOTE: 1. find Lowest Common ancestor (LCA)
#      2. get distance from LCA to each node, and add them together

class Solution:

    def minDis(self, root, a, b):
        lca = self.LCA(root, a, b)
        da = self.distance(lca, a, 0)
        db = self.distance(lca, b, 0)
        return da + db

    def LCA(self, root, a, b):
        if not root:
            return None
        if root.val == a.val or root.val == b.val:
            return root

        left = self.LCA(root.left, a, b)
        right = self.LCA(root.right, a, b)

        if left and right:
            return root
        elif left and not right:
            return left
        elif right and not left:
            return right
        return None

    def distance(self, root, node, step):
        if not node:
            return -1
        if root.val == node.val:
            return step
        left = self.distance(root.left, node, step+1)
        if left == -1:
            return self.distance(root.right, node, step+1)
        return left
