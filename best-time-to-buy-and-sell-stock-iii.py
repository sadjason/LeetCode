# encoding: utf-8

__author__ = 'zhangwei'

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0

        sell = [0] * n
        # sell[i]表示第i天卖掉股票（显然需要在i天前买入）的最大收益
        for i in xrange(1, n):
            p = prices[i] - prices[i-1]
            sell[i] = max(sell[i-1] + p, p)

        profits1 = sell
        # profits1[i]表示i天内卖掉的最大利润
        for i in xrange(1, n):
            profits1[i] = max(profits1[i], profits1[i-1])

        buy = [0] * n
        # buy[i]表示第i天买入股票（显然需要在i天后卖出）的最大收益
        for i in xrange(n-2, -1, -1):
            p = prices[i+1] - prices[i]
            buy[i] = max(buy[i+1] + p, p)

        profits2 = buy
        # profits2[i]表示第i天后买入股票的最大利益
        for i in xrange(n-2, -1, -1):
            profits2[i] = max(profits2[i+1], profits2[i])
        
        ret = 0
        for i in xrange(0, n):
            ret = max(ret, profits1[i] + profits2[i])
        return ret