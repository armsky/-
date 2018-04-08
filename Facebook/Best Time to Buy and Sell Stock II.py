"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you
must sell the stock before you buy again).

Have you met this question in a real interview?
Example
Given an example [2,1,2,0,1], return 2

"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        n = len(prices)
        pro = [0]
        for i in range(1, n):
            pro.append(max(0, prices[i] - prices[i-1]))
        return sum(pro)
