"""
Merge two given sorted integer array A and B into a new sorted integer array.
"""

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    # NOTE: Challenge, what is one array is very large and the other is small
    def mergeSortedArray(self, A, B):
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

    # NOTE: merge nums2 into nums1 as one sorted array, assume nums1 is big enough
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
