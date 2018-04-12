"""
Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Have you met this question in a real interview?
Example
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        m = len(A)
        n = len(A[0])
        t = len(B[0])
        res = [[0 for _ in range(t)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                for k in range(t):
                    res[i][k] += A[i][j] * B[j][k]
        return res
