"""
Given a string s, cut s into some substrings such that every substring is a
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
"""
class Solution:
    # @param s, a string
    # @return an integer

    # NOTE: DP Versino
    def minCut(self, s):
        if s == s[::-1]:
            return 0
        n = len(s)
        # Only to pass extream test cases
        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        # m[i][j] means s[i:j+1] is palindrome, only need to fill top right corner
        m = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    m[i][j] = 1
                else:
                    m[i][j] = self.is_palindrome(s, i, j)

        # dp[i] means min cut of s[:i]
        dp = [x-1 for x in range(n+1)]
        for i in range(n+1):
            for j in range(0, i):
                if m[j][i-1] == 1:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return 0
            i += 1
            j -= 1
        return 1

    #======================

    # DFS version, same as palindrome partitioning I
    # Got Time Limit Exceeded
    def minCut(self, s):
        if s == s[::-1]:
            return 0
        self.res = 0xffffffff
        self.dfs(s, [])
        return self.res

    def dfs(self, s, tmp):
        if s == '':
            self.res = min(self.res, len(tmp) - 1)
            return
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], tmp+[s[:i]])


    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return 0
            i += 1
            j -= 1
        return 1
