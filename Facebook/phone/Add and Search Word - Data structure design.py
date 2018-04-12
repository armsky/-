"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""
class TrieNode:

    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        return self.helper(word, self.root)

    def helper(self, word, node):
        if not word:
            if node.isWord:
                return True
            else:
                return False
        for c in word:
            if c != '.':
                if c not in node.children:
                    return False
                else:
                    node = node.children[c]
                    return self.helper(word[1:], node)
            else:
                nodes = node.children.values()
                for n in nodes:
                    if self.helper(word[1:], n):
                        return True
        return False
