"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Have you met this question in a real interview?
Example
Given a matrix

[
    [1,2],
    [3,4]
]
rotate it by 90 degrees (clockwise), return

[
    [3,1],
    [4,2]
]
"""
#NOTE:
#XXX: 1. 顺时针旋转需要对角线翻转加上上下翻转
#     2. 逆时针旋转需要对角线翻转加上左右翻转
class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        n = len(matrix)
        if n < 2:
            return matrix
        for i in range(n):
            for j in range(i+ 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
