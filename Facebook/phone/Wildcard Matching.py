"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Have you met this question in a real interview?
Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    #NOTE: DFS version, but got TLE
    def isMatch(self, s, p):
        if s == '':
            if p == '':
                return True
            elif p.startswith('*'):
                return self.isMatch(s, p[1:])
            else:
                return False
        if p == '':
            return False


        if s[0] == p[0] or p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        else:
            return False

    # DP version
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and j > 0:
                    dp[i][j] |= dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] in ['?', '*'])
                if i > 0 and j > 0:
                    dp[i][j] |= dp[i-1][j] and p[j-1] == '*'
                if j > 0:
                    dp[i][j] |= dp[i][j-1] and p[j-1] == '*'
        return dp[m][n]

    #NOTE: O(m*n) Solution
    def isMatch(self, s, p):
        si, pi, match = 0, 0, 0
        stari = -1
        while si<len(s):
            if pi<len(p) and (p[pi] == '?' or s[si] == p[pi]):
                si += 1
                pi += 1
            elif pi < len(p) and p[pi] == '*':
                stari = pi
                match = si
                pi += 1
            elif stari != -1:
                pi = stari + 1
                match += 1
                si = match
            else:
                return False
        while pi < len(p) and p[pi] == '*':
            pi += 1
        return pi == len(p)
