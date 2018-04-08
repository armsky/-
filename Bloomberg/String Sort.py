"""
Given a string, sort the string with the first keyword which is the most commonly
used characters and the second keyword which is the dictionary order.

 Notice
The length of string is less than 10000.
All characters are lowercase
Have you met this question in a real interview?
Example
Given str = “bloomberg”, return “bbooeglmr”.

Explanation:
'b' appears the most frequently, and the dictionary sequence is the smallest,
so it is ranked first, followed by 'o'.
Given str = “lintcode”, return “cdeilnot”.

Explanation:
All characters appear the same number of times, so directly in accordance with
the dictionary order.
"""
from collections import Counter

class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, str):
        d = Counter()

        def cmp(a, b):
            if d[a] == d[b]:
                if a < b:
                    return -1
                elif a == b:
                    return 0
                else:
                    return 1
            else:
                return d[b] - d[a] #XXX

        for c in str:
            d[c] += 1
        l = list(str)
        l.sort(cmp)
        return ''.join(l)
