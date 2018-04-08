"""
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when
we create the data structure.
"""
from heapq import heappop, heappush

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.len = 0
        self.q = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heappush(self.q, num)
        self.len += 1
        if self.len > self.k:
            heappop(self.q)
            self.len -= 1

    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.q, reverse=True)
