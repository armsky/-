"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

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
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    #NOTE: NOT a BST !!!
    def lowestCommonAncestor(self, root, A, B):
        if not root:
            return None
        if A.val == root.val or B.val == root.val:
            return root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left and not right:
            return left
        elif right and not left:
            return right
        elif left and right:
            return root
        else:
            return None
