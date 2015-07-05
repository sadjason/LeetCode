# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        paths = [[0] * n for x in xrange(m)]
        
        # 初始值
        paths[0][0] = 1
        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                break
            paths[i][0] = 1
        for j in xrange(1, n):
            if obstacleGrid[0][j] == 1:
                break
            paths[0][j] = 1

        # 状态转换方程
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[m-1][n-1]