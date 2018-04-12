"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(string s, string p)
Have you met this question in a real interview?
Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
class Solution(object):

    #NOTE: DP version
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return dp[m][n]


    #NOTE: DFS version, got TLE
    def isMatch(self, s, p):
        if s == '':
            if p == '':
                return True
            elif len(p) >= 2:
                return p[1] == '*' and self.isMatch(s, p[2:])
            else:
                return False
        if not p or not s:
            return False

        if len(p) >= 2 and p[1] == '*':
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:])
            else:
                return self.isMatch(s, p[2:])
        else:
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])

        return False
