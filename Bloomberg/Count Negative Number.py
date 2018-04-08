"""
Give a horizontally sorted and vertically sorted n * m matrix, find the number
of negative number.

 Notice
The size of given matrix is n x m, n <= 500, m <= 500.
In order to restrain the time complexity of the program, your program will run
10 ^ 5 times.
Have you met this question in a real interview?
Example
Given mat =

[
    [-5,-3,-1,0,1],
    [-2,-1,0,0,1],
    [0,11,12,12,14]
],
return 5.

Explanation:
There are only 5 negative number.
Given mat =

[
    [-50,-30,-10,-5],
    [-30,-20,-5,-1],
    [-10,-5,-1,0]
]
return 11。

Explanation:
There are only 11 negative number.
"""
class Solution:
    """
    @param nums: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, nums):
        n = len(nums[0])
        res = 0
        for arr in nums:
            while n > 0:
                if arr[n-1] < 0:
                    break
                n -= 1
            res += n
        return res
