# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        ret = 0
        for i in xrange(1, len(prices)):
            c = prices[i] - prices[i-1]
            if c > 0:
                ret += c
        return ret