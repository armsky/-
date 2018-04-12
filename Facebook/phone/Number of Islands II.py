"""
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

 Notice
0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Have you met this question in a real interview?
Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param: n: An integer
    @param: m: An integer
    @param: operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        if not m or not n:
            return []
        self.father = {}
        self.children = {}
        board = [[None for _ in range(m)] for _ in range(n)]
        res = []
        for point in operators: # in case dup point
            if not board[point.x][point.y]:
                board[point.x][point.y] = point
                self.father[point] = point
                self.children[point] = [point]
                self.check(n, m, point, board)
                res.append(len(self.children))
            else:
                res.append(res[-1])
        return res

    def check(self, n, m, point, board):
        a = [-1,1,0,0]
        b = [0,0,-1,1]
        for d in range(4):
            x = point.x+a[d]
            y = point.y+b[d]
            if 0 <=x<n and 0<=y<m and board[x][y] is not None:
                pointN = board[x][y]
                self.union(point, pointN)

    def find(self, point):
        if self.father[point] == point:
            return point
        return self.find(self.father[point])

    def union(self, pointA, pointB):
        fa = self.find(pointA)
        fb = self.find(pointB)
        if fa != fb:
            self.father[fa] = fb
            self.children[fb] += self.children[fa]
            del self.children[fa]
