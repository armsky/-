"""
There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend
of B, and B is a direct friend of C, then A is an indirect friend of C. And we
defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in
the class. If M[i][j] = 1, then the ith and jth students are direct friends with
each other, otherwise not. And you have to output the total number of friend
circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students
are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same
friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""
# NOTE: Version 1, update the friends relation at last
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        self.friends = [x for x in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.connect(i, j)
        circle = set()
        for i in range(n):
            self.friends[i] = self.find(self.friends[i])
            circle.add(self.friends[i])
        return len(circle)

    def find(self, a):
        if a == self.friends[a]:
            return a
        return self.find(self.friends[a])

    def connect(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.friends[fb] = fa

#NOTE: Version 2, do not update friends, only keep a counter
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        self.friends = [x for x in range(n)]
        self.circle = n
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.connect(i, j)

        return self.circle

    def find(self, a):
        if a == self.friends[a]:
            return a
        return self.find(self.friends[a])

    def connect(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.friends[fb] = fa
            self.circle -= 1

#NOTE: Version 3: DFS
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        visited = [0 for _ in range(n)]
        cnt = 0
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, M, visited)
                cnt += 1
        return cnt

    def dfs(self, i, M, visited):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(j, M, visited)
