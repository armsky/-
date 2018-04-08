"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible
for you to finish all courses?

Have you met this question in a real interview?
Example
Given n = 2, prerequisites = [[1,0]]
Return true

Given n = 2, prerequisites = [[1,0],[0,1]]
Return false
"""
from collections import deque, defaultdict

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        map = {} # store how many prerequisites left
        for i in range(numCourses):
            map[i] = 0
        pres = defaultdict(list) # store what other coures that require current course as prerequisite
        for (c, pc) in prerequisites:
            map[c] += 1
            pres[pc].append(c)

        q = deque()
        for c in range(numCourses):
            if map[c] == 0:
                q.append(c)
        cnt = 0
        while q:
            c = q.popleft()
            cnt += 1
            map[c] -= 1
            for p in pres[c]:
                map[p] -= 1
                if map[p] == 0:
                    q.append(p)

        if cnt == numCourses:
            return True
        return False
