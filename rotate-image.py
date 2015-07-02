# encoding: utf-8

__author__ = 'zhangwei'


# 递归版本
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        self.rotateMatrix(matrix, n, 1)

    # matrix表被旋转的matrix，layer表第几层
    def rotateMatrix(self, matrix, n, layer):
        if layer > n / 2:
            return
        i = layer-1
        cnt = n - (layer-1) * 2 - 1
        j = i
        while j < i + cnt:
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
            j += 1
        self.rotateMatrix(matrix, n, layer+1)


# 迭代版本