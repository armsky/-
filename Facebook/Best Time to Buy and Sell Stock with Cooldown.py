"""
Say you have an array for which the ith element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (ie, buy one and sell one share of the stock multiple times) with the
following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        # if sell prices[i], current profit
        sell = [0 for _ in range(n)]
        sell[1] = prices[1] - prices[0]
        # if cooldown in position i, current profit
        idle = [0 for _ in range(n)]
        for i in range(2, n):
            sell[i] = max(sell[i-1], idle[i-2]) + prices[i] - prices[i-1]
            idle[i] = max(sell[i-1], idle[i-1])
        return max(sell[-1], idle[-1])
