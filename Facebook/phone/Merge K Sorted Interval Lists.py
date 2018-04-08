"""
Merge K sorted interval lists into one sorted interval list. You need to merge
overlapping intervals too.

Have you met this question in a real interview?
Example
Given

[
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
Return

[(1,3),(4,8),(9,10)]
"""

from collections import defaultdict

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return []
        map = defaultdict(int)
        for l in intervals:
            for interval in l:
                map[interval.start] += 1
                map[interval.end] -= 1

        res = []
        start = end = None
        cnt = 0
        for t in sorted(map.keys()):
            cnt += map[t]
            if start is None and cnt > 0:
                start = t
            if start is not None and cnt <= 0:
                end = t
                interval = Interval(start, end)
                res.append(interval)
                start = None
        return res
