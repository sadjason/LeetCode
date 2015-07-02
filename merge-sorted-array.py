# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        # A中的元素向右移动n个位置
        for i in xrange(m):
            A[n+m-1-i] = A[m-1-i]
        
        # 合并A[n:m+n]和B[0:n]
        i, i1, i2 = 0, n, 0
        while i1 < n+m and i2 < n:
            if A[i1] > B[i2]:
                A[i], i2 = B[i2], i2+1
            else:
                A[i], i1 = A[i1], i1+1
            i += 1
        
        while i1 < m+n:
            A[i] = A[i1]
            i, i1 = i+1, i1+1
        
        while i2 < n:
            A[i] = B[i2]
            i, i2 = i+1, i2+1
        return