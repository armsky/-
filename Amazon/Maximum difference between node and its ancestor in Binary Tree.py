"""
Given a binary tree, we need to find maximum value we can get by subtracting value
of node B from value of node A, where A and B are two nodes of the binary tree
and A is an ancestor of B. Expected time complexity is O(n).
"""

#NOTE: find the min val of left subtree and right subtree
#      update the res
#      return the min val of (left, right, itself)
class Solution:

    def maxDiff(self, root):
        self.res = -0xffffffff

    def util(self, node):
        if not node:
            return 0xffffffff
        if not node.left and not node.right:
            return node.val
        minval = min(self.util(root.left), self.util(root.right))
        self.res = max(self.res, node.val - minval)
        return min(minval, node.val)
