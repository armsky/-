"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        rootidx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootidx+1], inorder[:rootidx])
        root.right = self.buildTree(preorder[rootidx+1:], inorder[rootidx + 1:])
        return root
