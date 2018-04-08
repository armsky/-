"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

How we serialize an undirected graph:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

   1
  / \
 /   \
0 --- 2
     / \
     \_/
"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from Queue import Queue

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if not node:
            return None

        map = {}
        all_nodes = self.getNodes(node)
        for n in all_nodes:
            map[n] = UndirectedGraphNode(n.label)

        for n in all_nodes:
            copy = map[n]
            for nb in n.neighbors:
                copy.neighbors.append(map[nb])
        return map[node]


    def getNodes(self, node):
        q = Queue()
        q.put(node)
        nodes = set([node])
        while q.qsize() > 0:
            node = q.get()
            for nb in node.neighbors:
                if nb not in nodes:
                    nodes.add(nb)
                    q.put(nb)
        return nodes
# Vesion 2: recursively
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        if node == None:
            return None
        if node.label in self.dict:
            return self.dict[node.label]
        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.cloneGraph(item))
        return root
