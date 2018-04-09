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
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
class TrieNode(object):

    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchFrom(word, self.root)

    def searchFrom(self, word, node):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                allChars = node.children.keys()
                for char in allChars:
                    if self.searchFrom(word[i+1:], node.children[char]):
                        return True
                return False
            else:
                if c in node.children:
                    node = node.children[c]
                else:
                    return False
        if node.isWord:
            return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
