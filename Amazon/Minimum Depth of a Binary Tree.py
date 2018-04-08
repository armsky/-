"""
Given a binary tree, find its minimum depth. The minimum depth is the number of
nodes along the shortest path from root node down to the nearest leaf node.

Note that the path must end on a leaf node. For example, minimum height of below
Binary Tree is also 2.

          10
        /
      5
"""
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if not root:
            return 0
        return self.getDepth(root, 0)

    def getDepth(self, root, depth):
        if not root:                        # None is not a leaf
            return 0xffffffff
        if not root.left and not root.right: # leaf node has no children
            return depth + 1
        left = self.getDepth(root.left, depth+1)
        right = self.getDepth(root.right, depth+1)
        return min(left, right)
