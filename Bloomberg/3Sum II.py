"""
Given n, find the number of solutions for all x, y, z that conforms to
x^2+y^2+z^2 = n.(x, y, z are non-negative integers)

 Notice
n <= 1000000
x, y, z satisfy (x <= y <= z), we can consider that is the same solution as
long as the three numbers selected are the same

Example
Given n = 0, return 1.

Explanation:
When x = 0, y = 0, z = 0, the equation holds.
Given n = 1, return 1.

Explanation:
When one of them is 1 and the remaining two are 0, there is a total of 1 solution.
"""
from math import sqrt

class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    def threeSum2(self, n):
        a = [x for x in range(int(sqrt(n)) + 1)]
        cnt = 0
        for i in range(len(a)):
            z = a[i]
            target = n - z**2
            cnt += self.twosum(a, target, i) # only search numbers that bigger than z
        return cnt

    def twosum(self, l, target, left):
        cnt = 0
        i = left
        j = len(l) - 1
        while i <= j:
            if l[i]**2 + l[j]**2 < target:
                i += 1
            elif l[i]**2 + l[j]**2 > target:
                j -= 1
            else:
                cnt += 1
                i += 1
        return cnt
