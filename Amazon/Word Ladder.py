"""
Given two words (start and end), and a dictionary, find the length of shortest
transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
 Notice
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
Have you met this question in a real interview?
Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    # NOTE: 记得把end word加进dict
    def ladderLength(self, start, end, dict):
        if not start or not end or not dict:
            return 0
        all_words = set(dict)
        all_words.add(end)
        q = [(start, 1)]
        while q:
            w, l = q.pop(0)
            if w == end:
                return l
            for i, c in enumerate(w):
                for e in 'abcdefghijklmnopqrstuvwxyz':
                    nw = w[:i] + e + w[i+1:]
                    if nw in all_words:
                        all_words.discard(nw) # remove the new word to avoid visited words
                        q.append((nw, l+1))

    # NOTE:优化：用bidirectional BFS
    
