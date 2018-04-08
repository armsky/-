"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA)
of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor
of both nodes.

 Notice
Assume two nodes are exist in tree.

Have you met this question in a real interview?
Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if root == p or root == q:
            return root
        if left and right:
            return root
        if left and not right:
            return left
        if right and not left:
            return right
        return None
