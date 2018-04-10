"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    #NOTE: Straight forward,
    def maxProfit(self, prices):
        if not prices:
            return 0
        # profit[0:n] = profit[0:i] + profit[i:n]
        left = [0 for _ in range(len(prices))]
        minp = prices[0]
        for i in range(1, len(prices)):
            minp = min(minp, prices[i])
            left[i] = max(left[i-1], prices[i] - minp)

        right = [0 for _ in range(len(prices))]
        maxp = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            maxp = max(maxp, prices[i])
            right[i] = max(right[i+1], maxp-prices[i])

        res = 0
        for i in range(len(prices)):
            res = max(res, left[i] + right[i])
        return res
