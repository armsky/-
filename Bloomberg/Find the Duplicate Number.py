"""
Given an array nums containing n + 1 integers where each integer is between 1
and n (inclusive), prove that at least one duplicate number must exist. Assume
that there is only one duplicate number, find the duplicate one.

 Notice
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
Have you met this question in a real interview?
Example
Given nums = [5,5,4,3,2,1] return 5
Given nums = [5,4,4,3,2,1] return 4
"""
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # NlogN:鸽子洞理论 (Pigeonhole Principle)
        #遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，
        #否则可以确定解落在(n / 2, n]范围内。
        n = len(nums) - 1
        l = 1
        r = n
        while l <= r:
            m = (l + r) >> 1
            cnt = sum([x<=m for x in nums])
            if cnt <= m:
                l = m + 1
            else:
                r = m - 1
        return l
