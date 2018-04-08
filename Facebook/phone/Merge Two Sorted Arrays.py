"""
Merge two given sorted integer array A and B into a new sorted integer array.
"""

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # NOTE: Challenge, what is one array is very large and the other is small
        from bisect import bisect_right

        if len(B) > len(A):
            return self.mergeSortedArray(B, A)

        i = 0
        res = []
        for num in B:
            pos = bisect_right(A, num)
            res += A[i:pos]
            res.append(num)
            i = pos
        res += A[i:]
        return res
