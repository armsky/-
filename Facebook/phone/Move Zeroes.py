"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    # Much simpler version
    def moveZeroes(self, nums):
        j = 0
        for i in range(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

    #NOTE: My version, too many if and else and easy to have bug
    #NOTE: Follow up: as less write as possible
    def moveZeroes(self, nums):
        n = len(nums)
        if n >= 2:
            i = 0
            j = 1
            while i < n and j < n:
                if i >= j:
                    j = i + 1
                if nums[i] == 0:
                    while j < n and nums[j] == 0:
                        j += 1
                    if j >= n:          #XXX: IMPORTANT!!!
                        break
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
