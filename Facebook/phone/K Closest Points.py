"""
Given some points and a point origin in two dimensional space, find k points out
of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance, sorted by
x-axis, otherwise sorted by y-axis.

Have you met this question in a real interview?
Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
"""
from heapq import heappush, heappop

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        q = []
        for point in points:
            distance = (point.x - origin.x)**2 + (point.y - origin.y)**2
            heappush(q, (distance,
                         point.x,
                         point.y,
                         point))
        res = []
        while k:
            res.append(heappop(q)[3])
            k -= 1
        return res

    # Optimize heap length, need max heap
    def kClosest(self, points, origin, k):
        q = []
        cnt = 0
        for point in points:
            distance = (point.x - origin.x)**2 + (point.y - origin.y)**2
            heappush(q, (-distance,
                         -point.x,
                         -point.y,
                         point))
            cnt += 1
            if cnt > k:
                heappop(q)

        res = []
        while k:
            res.append(heappop(q)[3])
            k -= 1
        return res[::-1]
