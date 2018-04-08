"""
Given a string s, partition s such that every substring of the partition is a p
alindrome.

Return all possible palindrome partitioning of s.

Have you met this question in a real interview?
Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]"""
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        self.res = []
        n = len(s)
        self.dfs(s, [])
        return self.res

    def dfs(self, s, tmp):
        if len(s) == 0:
            self.res.append(tmp)
            return
        for j in range(1, len(s) + 1):
            if self.isPalindrome(s[:j]):
                self.dfs(s[j:], tmp+[s[:j]])


    def isPalindrome(self, s):
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
