"""
Given a string source and a string target, find the minimum window in source which
will contain all the characters in target.

 Notice
If there is no such window in source that covers all characters in target, r
eturn the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in source.

Have you met this question in a real interview?
Clarification
Should the characters in minimum window has the same order in target?

Not necessary.
Example
For source = "ADOBECODEBANC", target = "ABC", the minimum window is "BANC"
"""
from collections import Counter

class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        if not source:
            return ''
        minlen = len(source)
        res = ''
        map = Counter()
        target_map = Counter()
        for t in target:
            target_map[t] += 1
        window = ''
        i = 0
        while i < len(source):
            c = source[i]
            window += c
            map[c] += 1
            while self.contains(map, target_map):
                if len(window) <= minlen: # need to be <=
                    minlen = len(window)
                    res = window
                d = window[0]
                window = window[1:]
                map[d] -= 1
                if map[d] < 1:
                    del map[d]
            i += 1
        return res

    def contains(self, map, target_map):
        for t, cnt in target_map.items():
            if t in map and map[t] >= target_map[t]:
                continue
            else:
                return False
        return True
