"""
Given a string, find the length of the longest substring without repeating characters.

Have you met this question in a real interview?
Example
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        i = j = 0
        d = set()
        res = tmp = 0
        while j < len(s):
            while j < len(s) and s[j] not in d:
                d.add(s[j])
                tmp += 1
                j += 1
            if tmp > res:
                res = tmp
            if j >= len(s):
                break
            while i < j and s[i] != s[j]:
                d.remove(s[i])
                i += 1
                tmp -= 1
            i += 1
            j += 1
        return res

    # Jiuzhang Version
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        last = {} # character latest position
        left = 0  # current subarray's left boundray
        res = 0
        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            last[s[i]] = i
            res = max(res, i - left + 1)
        return res
