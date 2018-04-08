"""
Given an directed graph, a topological order of the graph nodes is defined as f
ollow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

 Notice
You can assume that there is at least one topological order in the graph.

Have you met this question in a real interview?
Clarification
Learn more about representation of graphs

Example
For graph as follow:

picture

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
"""
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        n = len(graph)
        map = {}
        for node in graph:
            map[node] = 0
        for node in graph:
            for n in node.neighbors:
                map[n] += 1

        res = []
        for node in graph:
            if map[node] == 0:
                self.bfs(node, map, res)
        return res

    def bfs(self, node, map, res):
        res.append(node)
        map[node] -= 1
        for nb in node.neighbors:
            map[nb] -= 1
            if map[nb] == 0:
                self.bfs(nb, map, res)
            
