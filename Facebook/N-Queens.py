"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
# LeetCode 51
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(0, [], [], [], n, [])
        return self.res

    # down: 纵向不重合
    # left：左斜不重合（i+j)
    # right：右斜不重合 （i-j)
    def dfs(self, i, down, left, right, n, tmp):
        if i == n:
            self.res.append(list(tmp))
            return

        for j in range(n):
            dots = ['.' for _ in range(n)]
            if not tmp or (j not in down and i+j not in left and i-j not in right):
                dots[j] = 'Q'
                tmp.append(''.join(dots))
                self.dfs(i+1, down + [j], left + [i+j], right + [i-j], n, tmp)
                tmp.pop()
        return
