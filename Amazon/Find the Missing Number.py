"""
Given an array contains N numbers of 0 .. N, find which number doesn't exist in
the array.

Have you met this question in a real interview?
Example
Given N = 3 and the array [0, 1, 3], return 2.
"""

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    # Version 1
    def findMissing(self, nums):
        n = len(nums)
        # s = sum([num for num in range(n+1)])
        s = n * (n+1) / 2
        for num in nums:
            s -= num
        return s

    # Version 2, XOR
    # 1) XOR all the array elements, let the result of XOR be X1.
    # 2) XOR all numbers from 1 to n, let XOR be X2.
    # 3) XOR of X1 and X2 gives the missing number.
    def findMissing(self, nums):
        n = len(nums)
        x = nums[0]
        for i in range(1, n):
            x ^= nums[i]
        y = 0
        for i in range(n+1):
            y ^= i
        return x^y
