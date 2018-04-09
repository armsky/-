"""
Given a char array representing tasks CPU need to do. It contains capital letters
A to Z where different letters represent different tasks.Tasks could be done
without original order. Each task could be done in one interval. For each interval,
CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same
tasks, there must be at least n intervals that CPU are doing different tasks or
just be idle.

You need to return the least number of intervals the CPU will take to finish all
the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
from collections import Counter
from heapq import heappop, heappush

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = Counter()
        q = []
        for t in tasks:
            map[t] += 1
        for t, cnt in map.items():
            heappush(q, (-cnt, t))

        res = 0
        while q:
            k = n+1
            tmp = []
            while k > 0 and q:
                ne_cnt, t = heappop(q)
                ne_cnt += 1
                tmp.append((ne_cnt, t))
                res += 1
                k -= 1
            for ne_cnt, t in tmp:
                if ne_cnt < 0:
                    heappush(q, (ne_cnt, t))
            if not q: #NOTE: if q is empty, break to avoid  last unwanted idles
                break
            if k > 0:
                res += k

        return res
