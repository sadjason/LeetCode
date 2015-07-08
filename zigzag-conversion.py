# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @return a string
    def convert(self, s, nRows):
        T = 1
        if nRows > 1:
            T = 2 * nRows - 2
        result, n = '', len(s)

        for row in range(0, nRows):
            i, j = row, T - row
            while i < n or j < n:
                if i < j:
                    result, i = result+s[i], i+T
                elif j < i:
                    result, j = result+s[j], j+T
                else:
                    result, i, j = result+s[i], i+T, j+T

        return result