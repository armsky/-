"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.
"""
class Solution(object):
    # Recursive
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # Level order
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        i = 1
        s = [root]

        while s:
            ss = []
            for node in s:
                if not node.left and not node.right:
                    return i
                if node.left:
                    ss.append(node.left)
                if node.right:
                    ss.append(node.right)
            i += 1
            s = ss
