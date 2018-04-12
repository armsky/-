"""
Given a digit string excluded 01, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Cellphone

 Notice
Although the above answer is in lexicographical order, your answer could be in any order you want.

Have you met this question in a real interview?
Example
Given "23"

Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

class Solution:
    map = ['','','abc','def','ghi','jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    res = []
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if digits == '':
            return []
        self.dfs(digits, '')
        return self.res


    def dfs(self, digits, tmp):
        if not digits:
            self.res.append(tmp)
            return
        d = digits[0]
        chars = self.map[int(d)]
        for char in chars:
            self.dfs(digits[1:], tmp+char)
