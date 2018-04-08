"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the
ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it
is impossible to finish all courses, return an empty array.

Have you met this question in a real interview?
Example
Given n = 2, prerequisites = [[1,0]]
Return [0,1]

Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
Return [0,1,2,3] or [0,2,1,3]
"""
from collections import defaultdict, deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        map = {}
        for i in range(numCourses):
            map[i] = 0
        pres = defaultdict(list)
        for (c, pc) in prerequisites:
            map[c] += 1
            pres[pc].append(c)
        q = deque()
        for i in range(numCourses):
            if map[i] == 0:
                q.append(i)
        res = []
        while q:
            i = q.popleft()
            res.append(i)
            map[i] -= 1
            for c in pres[i]:
                map[c] -= 1
                if map[c] == 0:
                    q.append(c)

        if len(res) == numCourses:
            return res
        return []
