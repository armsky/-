"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Have you met this question in a real interview?
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
"""
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not target:
            return False
        m,  n = len(matrix), len(matrix[0])
        i, j = 0, n-1   # From top right corner
        while i < m and j >= 0:
            if matrix[i][j] < target:
                i += 1
            if matrix[i][j] > target:
                j -= 1
            if matrix[i][j] == target:
                return True
        return False
