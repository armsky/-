"""
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

 Notice
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

Have you met this question in a real interview?
Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        res = set()
        numbers.sort()
        for i in range(len(numbers)):
            target = numbers[i]
            a = numbers[:i] + numbers[i+1:]
            tmp = self.twosum(a, -target)
            if len(tmp) > 0:
                for t in tmp:
                    t.append(target)
                    res.add(tuple(sorted(t)))
        return sorted(list(res)) # Also required sorted

    def twosum(self, a, target):
        # may have multiple ans
        res = []
        i = 0
        j = len(a) - 1
        while i < j:
            if a[i] + a[j] > target:
                j -= 1
            elif a[i] + a[j] < target:
                i += 1
            else:
                res.append([a[i], a[j]])
                i += 1
        return res
                
