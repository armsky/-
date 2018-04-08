"""
There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from the
dictionary, where words are sorted lexicographically by the rules of this new
language. Derive the order of letters in this language.

 Notice
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the
given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in lexicographical order
Have you met this question in a real interview?
Example
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf"

Given the following words in dictionary,

[
  "z",
  "x"
]
"""
from heapq import heappop, heappush

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph = self.constructGraph(words)
        return self.topologicalSorting(graph)

    def constructGraph(self, words):
        graph = {}
        #create nodes
        for i in range(len(words)):
            for j in range(len(words[i])):
                graph[words[i][j]] = set()

        #create edges
        for i in range(len(words) - 1):
            index = 0
            while index < len(words[i]) and index < len(words[i+1]):
                if words[i][index] != words[i+1][index]:
                    graph[words[i][index]].add(words[i+1][index])
                    break
                index += 1
        return graph

    def getIndegree(self, graph):
        indegree = {}
        for c in graph.keys():
            indegree[c] = 0
        for c in graph.keys():
            for v in graph[c]:
                indegree[v] = indegree[v] + 1
        return indegree

    def topologicalSorting(self, graph):
        indegree = self.getIndegree(graph)
        q = []
        for u in indegree.keys():
            if indegree[u] == 0:
                heappush(q, u)
        s = ''
        print graph
        while q:
            head = heappop(q)
            s += head
            for neighbor in graph[head]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(q, neighbor)

        if len(s) != len(indegree):
            return ''
        return s
