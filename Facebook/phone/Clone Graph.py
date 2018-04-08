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

# NOTE: Follow up: what is node value can be duplicate
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        map = {}
        q = [node]
        copy = UndirectedGraphNode(node.label)
        map[node] = copy
        while q:
            n = q.pop(0)
            for nb in n.neighbors:
                if nb not in map:
                    cp = UndirectedGraphNode(nb.label)
                    map[nb] = cp
                    q.append(nb)

        for n in map.keys():
            for nb in n.neighbors:
                map[n].neighbors.append(map[nb])
        return copy
