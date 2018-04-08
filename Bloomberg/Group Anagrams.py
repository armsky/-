"""
Given an array of strings, group anagrams together.

 Notice
All inputs will be in lower-case.

Have you met this question in a real interview?
Example
Given strs = ["eat", "tea", "tan", "ate", "nat", "bat"],
Return
[
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
]
"""
class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            key = ''.join(sorted(word)) # sorted(str) will becomes a list
            if key not in d:
                d[key] = []
            d[key].append(word)
        return [sorted(v) for v in d.values()]
