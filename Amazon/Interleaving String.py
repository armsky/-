"""
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving
of s1 and s2.

Have you met this question in a real interview?
Example
For s1 = "aabcc", s2 = "dbbca"

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    # NOTE: DFS version.
    #       Use invalid[][] to cache s1[0:i] and s[0:j] can not form s3[0:i+j]
    #       Use invalid not valid to cache because invalid is more common
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        invalid = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        return self.dfs(s1, s2, s3, 0, 0, 0, invalid)

    def dfs(self, s1, s2, s3, i, j, k, invalid):
        if invalid[i][j]:
            return False
        if k == len(s3):
            return True
        valid = (i < len(s1) and s1[i] == s3[k] and self.dfs(s1, s2, s3, i+1, j, k+1, invalid)) or \
                (j < len(s2) and s2[j] == s3[k] and self.dfs(s1, s2, s3, i, j+1, k+1, invalid))
        if not valid:
            invalid[i][j] = True
        return valid
    #================================================
    # NOTE: BFS version
    def isInterleave(self, s1, s2, s3):
        m, n, l = len(s1), len(s2), len(s3)
        if m+n != l:
            return False
        q = [(0, 0)]
        visited = set((0, 0))
        while q:
            i, j = q.pop(0)
            if i + j == l:
                return True
            if i < m and s1[i] == s3[i+j] and (i+1, j) not in visited:
                q.append((i+1, j))
                visited.add((i+1, j))
            if j < n and s2[j] == s3[i+j] and (i, j+1) not in visited:
                q.append((i, j+1))
                visited.add((i, j+1))
        return False

    #================================================
    # NOTE: DP Version
    def isInterleave(self, s1, s2, s3):
        def isInterleave(self, s1, s2, s3):
        m, n, l = len(s1), len(s2), len(s3)
        if m+n != l:
            return False
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
                           (dp[i][j-1] and s2[j-1] == s3[j-1+i])
        return dp[m][n]
