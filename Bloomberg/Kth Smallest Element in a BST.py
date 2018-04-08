"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 Notice
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Have you met this question in a real interview?
Example
Given root = {1,#,2}, k = 2, return 2.
"""
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        self.q = []
        self.inorder(root)
        return self.q[k-1]


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.q.append(root.val)
        self.inorder(root.right)
