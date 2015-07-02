# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return []
        cols = len(matrix[0])
        if cols == 0:
            return []
        
        ret = [0] * (rows * cols)
        
        preDir = 4  # 1 - right, 2 - down, 3 - left, 4 - up
        row = 0
        col = -1
        index = 0
        while index < rows * cols:
            if preDir == 4:     # 向右
                col += 1
                for x in xrange(cols - col * 2):
                    ret[index] = matrix[row][col]
                    col += 1
                    index += 1
                col -= 1
                preDir = 1
            elif preDir == 1:   # 向下
                row += 1
                for x in xrange(rows - row * 2):
                    ret[index] = matrix[row][col]
                    row += 1
                    index += 1
                row -= 1
                preDir = 2
            elif preDir == 2:   # 向左
                row += 1
                for x in xrange(cols - (cols-1-col) * 2):
                    ret[index] = matrix[row][col]
                    col -= 1
                    index += 1
                col += 1
                preDir = 3
            elif preDir == 3:   # 向上
                row -= 1
                for x in xrange(rows - (rows-1-row)*2):
                    ret[index] = matrix[row][col]
                    row -= 1
                    index += 1
                row += 1
                preDir = 4
        return ret