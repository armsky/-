"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Have you met this question in a real interview?
Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
"""
#NOTE: fibonacci
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        dp = [0,1,2]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
