"""
Determines whether a binary representation of a non-negative integer n is a palindrome

 Notice
0 <= n <= 2^32 - 1
Have you met this question in a real interview?
Example
Given n = 0, return True

Explanation:
The binary representation of 0 is: 0
Given n = 3, return True

Explanation:
The binary representation of 3 is: 11
Given n = 4, return False

Explanation:
The binary representation of 4 is: 100
Given n = 6, return False

Explanation:
The binary representation of 6 is: 110
"""
class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        ns = bin(n)[2:]
        for i in range(len(ns)):
            if ns[i] != ns[-i-1]:
                return False
        return True
