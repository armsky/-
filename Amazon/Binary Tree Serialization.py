class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        q = Queue()
        q.put(root)
        data = []
        while q.qsize() > 0:
            node = q.get()
            if node:
                data.append(node)
                q.put(node.left)
                q.put(node.right)
            else:
                data.append(None)
        # self.printTree(root)
        self.printData(data)
        return data


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        n = len(data)
        if n == 0:
            return None
        root = data[0]
        i = 0
        j = 0
        while j < len(data) -1: #注意此处i是如何递增的
            node = data[j]
            if node:
                node.left = data[i*2 + 1]
                node.right = data[i*2 + 2]
                i += 1
            j += 1
        return root
