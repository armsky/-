"""
Given a number n, we need to find the sum of all the elements from all possible
subsets of a set formed by first n natural numbers.

Have you met this question in a real interview?
Example
Given n = 2, return 6
Possible subsets are {{1}, {2}, {1, 2}}. Sum of elements in subsets
is 1 + 2 + 1 + 2 = 6

Given n = 3, return 24
Possible subsets are {{1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
Sum of subsets is :
1 + 2 + 3 + (1 + 2) + (1 + 3) +
(2 + 3) + (1 + 2 + 3)
"""
class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        a = [x for x in range(1, n+1)]
        self.res = 0
        self.dfs(a, 0, n-1, 0)
        return self.res


    def dfs(self, a, l, r, total):
        if l > r:
            self.res += total
            return
        # subset including a[l]
        self.dfs(a, l+1, r, total+a[l])
        # subset not including a[l]
        self.dfs(a, l+1, r, total)
