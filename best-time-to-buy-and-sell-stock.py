# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        sell = [0] * n      # sell[i]表示第i天卖掉股票的最大收益（显然股票需要在第i天前买入）
        ret = 0
        for i in xrange(1, n):
            p = prices[i] - prices[i-1]
            sell[i] = max(sell[i-1]+p, p)
            ret = max(sell[i], ret)
        return ret


# 简化版本
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        ret, profit = 0, 0
        ret = 0
        for i in xrange(1, len(prices)):
            p = prices[i] - prices[i-1]
            profit = max(profit+p, p)
            ret = max(profit, ret)
        return ret