"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1
"""
from collections import defaultdict

class Solution:

    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for i in range(len(s)):
            c = s[i]
            if d[c] < 2:
                return i
        return -1
