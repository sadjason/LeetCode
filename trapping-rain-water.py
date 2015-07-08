# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} heights
    # @return {integer}
    def trap(self, heights):
        begin, end = 0, len(heights) - 1
        ret, level = 0, 0   # ret表示返回值，level表示当前的最高水平面
        while begin < end:
            level = max(level, min(heights[begin], heights[end]))
            if heights[begin] <= heights[end]:
                ret += (level - heights[begin])
                begin += 1
            else:
                ret += (level - heights[end])
                end -= 1

        return ret