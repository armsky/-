"""
You are given a library with n words (w[0], w[1], ...,w[n-1]). You choose a word
from it, and in each step, remove one letter from this word only if doing so yields
another word in the library. What is the longest possible chain of these removal steps?

Constraints:
1 <= n <= 50000
1 <= the length of each string in w <= 50
Each string is composed of lowercase ascii letters only
The function should take in an array of strings w as its argument and should
return a single integer representing the length of the longest chain of character
removals possible.

Example input/output
a
b
ba
bca
bda
bdca

Calling the function on the input above should output 4. The longest possible
chain is "bdca" -> "bca" -> "ba" -> "a".
"""
def longestChain(words):
    if not words:
        return 0
    words.sort(key=len)
    max_len = 0
    d = {}
    for word in words:
        if len(word) < max_len:
            continue
        d[word] = 1
        word_len = findChainLength(word, d)
        max_len = max(word_len, max_len)
    return max_len

def findChainLength(word, d):
    if len(word) == 1:
        return 1
    res = 1
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in d:
            res = max(res, findChainLength(new_word, d) + 1)
    return res

w  = [ "a",  "b",  "ba", "bca", "bda", "bdca" ]
print longestChain(w)
