"""
Find the kth smallest number in at row and column sorted matrix.

Have you met this question in a real interview?
Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5
"""
from heapq import heappush, heappop

class Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        q = []
        # in heapq you can use tuples, and it will sort by the first element of the tuple:
        heappush(q, (matrix[0][0], 0, 0))
        used = {(0,0): 1}
        res = None
        while k > 0:
            res, i, j = heappop(q)
            self.getDown(matrix, i, j, q, used)
            self.getRight(matrix, i, j, q, used)
            k -= 1
        return res

    def getDown(self, matrix, i, j, q, used):
        if i+1 < len(matrix):
            i += 1
            if (i,j) not in used:
                heappush(q, (matrix[i][j], i, j))
                used[(i,j)] = 1

    def getRight(self, matrix, i, j, q, used):
        if j+1 < len(matrix[0]):
            j += 1
            if (i,j) not in used:
                heappush(q, (matrix[i][j], i, j))
                used[(i,j)] = 1      
