# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0

        paths = [[1] * n for x in xrange(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[m-1][n-1]