"""
Given an integer array, find the top k largest numbers in it.
"""
from heapq import heappop, heappush

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    # Version 1: use n length max heap, Time: O(nlogn), Space: O(n)
    def topk(self, nums, k):
        q = []
        for n in nums:
            heappush(q, -n)

        res = []
        while k > 0:
            if q:
                res.append(-heappop(q))
            else:
                break
            k -= 1
        return res

    # Version 2: k length, min heap, Time: O(n + (n-k)logk), Space O(k)
    def topk(self, nums, k):
        q = []
        lq = 0
        for n in nums:
            heappush(q, n)
            lq += 1
            if lq > k:
                heappop(q)
                lq -= 1

        return sorted(q, reverse=True)
