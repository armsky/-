"""
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty
string "".

If there are multiple such windows, you are guaranteed that there will always be
only one unique minimum window in S.

"""
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ''

        minlen = 0xfffffff
        map = Counter()
        target = Counter()
        for c in t:
            target[c] += 1

        win = ''
        res = ''
        i = 0
        while i < len(s):
            win += s[i]
            map[s[i]] += 1
            while self.contains(map, target):
                if len(win) <= minlen:
                    minlen = len(win)
                    res = win
                c = win[0]
                win = win[1:]
                map[c] -= 1
                if map[c] < 0 :
                    del map[c]

            i += 1

        return res


    def contains(self, map, target):
        for c, cnt in target.items():
            if map[c] >= cnt:
                continue
            else:
                return False
        return True
