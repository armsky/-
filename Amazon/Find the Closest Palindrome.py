"""
Given an integer n, find the closest integer (not including itself), which is a
palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""
# Leetcode HARD
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n) == 1:
            return str(int(n)-1)
        l = len(n)
        candidates = set([10**l + 1, 10**(l-1) - 1])
        prefix = n[:(l+1)/2]
        for k in [-1, 0, 1]:
            num = int(prefix) + k
            if l % 2 == 1:
                candidate = str(num) + str(num)[:-1][::-1]
            else:
                candidate = str(num) + str(num)[::-1]
            if int(candidate) != 0:
                candidates.add(int(candidate))
        candidates.discard(int(n))

        # return str(min(candidates, key=lambda x: (abs(x - int(n)), x)))
        minabs = int(n)
        res = int(n)
        print candidates
        for c in candidates:
            if abs(c - int(n)) < minabs:
                minabs = abs(c - int(n))
                res = [c]
            elif abs(c - int(n)) == minabs:
                res.append(c)
        return str(min(res))
