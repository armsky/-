"""
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Have you met this question in a real interview?
Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
"""
# BFS
class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        a = [-1,1,0,0]
        b = [0,0,-1,1]
        s = []
        cnt = 0
        visit = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visit[i][j]:
                    visit[i][j] = 1
                    if grid[i][j] == 1:
                        cnt += 1
                        s.append((i,j))
                        while s:
                            ii, jj = s.pop()
                            for k in range(4):
                                x = ii + a[k]
                                y = jj + b[k]
                                if x >= 0 and x < m and y>=0 and y < n and visit[x][y]==0 and grid[x][y]==1:
                                    s.append((x,y))
                                    visit[x][y] = 1
        return cnt
