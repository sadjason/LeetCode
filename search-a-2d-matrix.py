# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        
        start, stop = 0, rows*cols
        while start < stop:
            if stop-start <= 2:
                if matrix[start/cols][start%cols] == target \
                or matrix[(stop-1)/cols][(stop-1)%cols] == target:
                    return True
                return False
            mid = (start + stop) / 2
            midValue = matrix[mid/cols][mid%cols]
            if midValue == target:
                return True
            elif midValue > target:
                stop = mid
            else:
                start = mid+1