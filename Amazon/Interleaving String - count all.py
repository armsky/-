"""
Given two strings str1 and str2, write a function that prints all interleavings
of the given two strings. You may assume that all characters in both strings are
different

Example:

Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

Input: str1 = "AB",  str2 = "C"
Output:
    ABC
    ACB
    CAB
"""
class Solution:
    def getAllInterLeaving(self, a, b):
        self.res = []
        self.util(a, b, len(a), len(b), '')
        return self.res

    def util(self, a, b, m, n, tmp):
        if m == n == 0:
            self.res.append(tmp)
        if m != 0:
            tmp += a[0]
            self.util(a[1:], b, m - 1, n, tmp)
            tmp = tmp[:-1]
        if n != 0:
            tmp += b[0]
            self.util(a, b[1:], m, n - 1, tmp)
            # tmp = tmp[:-1]
