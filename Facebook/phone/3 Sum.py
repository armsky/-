"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):

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


    #NOTE: follow up: what if not sorting
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i, n in enumerate(nums):
            tmp = self.twoSum(nums[i+1:], 0-nums[i])
            for one in tmp:
                if one not in res:
                    res.append(one)

        return res

    def twoSum(self, nums, t):
        d = {}
        res = []
        for n in nums:
            if t-n not in d:
                d[n] = 1
            else:
                res.append(sorted([0-t, t-n, n]))
        return res
