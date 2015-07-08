# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} heights
    # @return {integer}
    def maxArea(self, heights):
        ret = 0
        i, j = 0, len(heights)-1
        while i < j:
            h = min(heights[i], heights[j])
            ret = max(ret, h * (j-i))
            if h == heights[i]:
                i += 1
            else:
                j -= 1
        return ret