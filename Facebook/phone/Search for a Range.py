"""
Given an array of integers sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return [-1, -1]
        # search left bound
        i = 0
        j = n-1
        while i + 1 < j:
            m = (i + j) / 2
            if target > nums[m]:
                i = m
            else:
                j = m

        if nums[i] == target:
            left = i
        elif nums[j] == target:
            left = j
        else:
            return [-1,-1]

        #seach right bound
        i = left
        j = n-1
        while i + 1 < j:
            m = (i + j) / 2
            if target < nums[m]:
                j = m
            else:
                i = m
        if nums[j] == target:
            right = j
        else:
            right = i
        return [left, right]
